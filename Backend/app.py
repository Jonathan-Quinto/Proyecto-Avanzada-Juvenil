from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from db_connection import get_connection  # Importamos desde tu archivo externo
from datetime import datetime
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Decorador para verificar rol master
def master_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_role') == 'master':
            flash('Acceso restringido: se requieren privilegios de administrador', 'danger')
            return redirect(url_for('inicio'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/eventos_añadir', methods=['POST'])
@master_required
def eventos_añadir():
    try:
        required_fields = ['titulo', 'lugar', 'fecha', 'hora_inicio', 'hora_fin']
        if not all(field in request.form for field in required_fields):
            return jsonify({"success": False, "message": "Faltan campos requeridos"}), 400
        
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO Eventos (
                titulo, descripcion, lugar, fecha, hora_inicio, hora_fin, 
                destacado, id_usuario
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            request.form['titulo'],
            request.form.get('descripcion', ''),
            request.form['lugar'],
            request.form['fecha'],
            request.form['hora_inicio'],
            request.form['hora_fin'],
            1 if request.form.get('destacado') == '1' else 0,
            session.get('user_id')
        )
        
        cursor.execute(query, params)
        conn.commit()
        
        return jsonify({
            "success": True,
            "message": "Evento creado exitosamente",
            "evento_id": cursor.execute("SELECT SCOPE_IDENTITY()").fetchval()
        })
        
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        if 'conn' in locals():
            conn.close()

@app.route('/api/eventos')
def api_eventos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                id, titulo, descripcion, lugar, 
                CONVERT(varchar, fecha, 23) as fecha,
                hora_inicio, hora_fin
            FROM Eventos 
            WHERE fecha >= CAST(GETDATE() AS DATE)
            ORDER BY fecha, hora_inicio
        """)
        
        eventos = [{
            "title": row.titulo,
            "start": f"{row.fecha}T{row.hora_inicio}",
            "end": f"{row.fecha}T{row.hora_fin}",
            "location": row.lugar,
            "description": row.descripcion
        } for row in cursor]
        
        return jsonify(eventos)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals():
            conn.close()


@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if login_usuario(email, password):
            session['user_logged_in'] = True
            session['user_email'] = email
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('fullName')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if registrar_usuario(nombre, email, password):
            flash('Registro exitoso. Por favor inicia sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error en el registro. El correo ya existe o hay un problema con el servidor.', 'danger')
    
    return render_template('registro.html')
@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

app.route('/eventos_añadir', methods=['GET', 'POST'])
def eventos_añadir():
    return render_template('eventos_añadir.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)