from src import app
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .api.login.endpoints import getOne
from .models.entities.persona import Persona

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['password']
        
        data = {'correo': correo, 'contrasena': contrasena}
        
        with app.test_request_context(json=data):
            response = getOne()
        
        if response.status_code == 200:
            data = response.get_json()
            
            logged = Persona(data['id'], data['rol'], 0, 0, 0, 0, 0, data['correo'], data['contrasena'])
            
            if logged and logged.cont_per:
                if logged.id_rol == 'Administrador':
                    login_user(logged)
                    return redirect(url_for('admin.index'))
        else:
            return render_template('auth/login.html', error='Credenciales incorrectas')
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def status401(error):
    return redirect(url_for('login'))

def status404(error):
    return "<h1>Pagina no encontrada</h1>"