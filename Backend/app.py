from flask import Flask, render_template, request, redirect, url_for, flash, session
from login import login_usuario
from registro_usuario import registrar_usuario
from subir_imagen import actualizar_imagen_usuario
import os
from datetime import datetime

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')

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