from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required
from ...api.login.endpoints import getAll


admin = Blueprint('admin', __name__)

@admin.route('/')
@login_required
def index():
    return redirect(url_for('admin.home'))
    
@admin.route('/home')
@login_required
def home():
    try:
        response = getAll()
        if response.status_code == 200:
            objeto = response.json
            
            return render_template('admin/index.html', datos = objeto)
        else:
            return render_template('app.index', error = 'Error al obtener los datos de usuarios')
    except Exception as e:
        return render_template('app.index', error=str(e))