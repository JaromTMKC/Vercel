from flask import Flask
from flask_login import LoginManager
#from flask_wtf.csrf import CSRFProtect
from src.config import DevelopmentConfig
from src.models.modelPersona import ModelPersona

#csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#csrf.init_app(app)

db = DevelopmentConfig.conection()
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return ModelPersona.readxID(db, id)

from src.views import status401, status404
from src.api.login.endpoints import api
from src.routes.admin.views import admin

app.register_blueprint(api, url_prefix = '/api')
app.register_blueprint(admin, url_prefix = '/admin')

app.register_error_handler(401, status401)
app.register_error_handler(404, status404)
