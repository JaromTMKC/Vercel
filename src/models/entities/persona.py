from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Persona(UserMixin):
    def __init__(self, id_per, id_rol, nomb_per, apel_per, dni_per, tele_per, coun_per, corr_per, cont_per) -> None:
        self.id_per = id_per
        self.id_rol = id_rol
        self.nomb_per = nomb_per
        self.apel_per = apel_per
        self.dni_per = dni_per
        self.tele_per = tele_per
        self.coun_per = coun_per
        self.corr_per = corr_per
        self.cont_per = cont_per
    
    def get_id(self):
        return str(self.id_per)
    
    def to_JSON(self):
        return {
            'id' : self.id_per,
            'rol' : self.id_rol,
            'nombre' : self.nomb_per,
            'apellido' : self.apel_per,
            'dni' : self.dni_per,
            'telefono' : self.tele_per,
            'codigoUniversitario' : self.coun_per,
            'correo' : self.corr_per,
            'contrasena' : self.cont_per
        }

    @classmethod
    def check(cls, hashedP, password):
        return check_password_hash(hashedP, password)