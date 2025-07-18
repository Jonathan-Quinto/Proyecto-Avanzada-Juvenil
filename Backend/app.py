from flask import Flask, render_template, request, redirect, url_for, flash, session
from login import login_usuario
from registro_usuario import registrar_usuario
from subir_imagen import actualizar_imagen_usuario
import os

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')
app.secret_key = 'tu_clave_secreta_aqui'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')

# Rutas principales
@app.route('/')
def inicio():
    return render_template('Inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email == "admin@example.com" and password == "password":
            session['user_logged_in'] = True
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('Login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        flash('Registro exitoso. Por favor inicia sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('Registro.html')

@app.route('/tienda')
def tienda():
    return render_template('Tienda.html')

@app.route('/eventos')
def eventos():
    return render_template('Eventos.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/logout')
def logout():
    session.pop('user_logged_in', None)
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
