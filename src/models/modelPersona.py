from .entities.persona import Persona

class ModelPersona():

    @classmethod
    def readOne(cls, db, user):
        try:
            cursor = db.cursor()
            sql = "SELECT p.id_per, p.corr_per, p.cont_per, r.nomb_rol FROM Persona p INNER JOIN Rol R ON p.id_rol = r.id_rol WHERE p.corr_per = '{}';".format(user.corr_per)
            
            cursor.execute(sql)
            row = cursor.fetchone()
            
            if row != None:
                user = Persona(row[0], row[3], 0, 0, 0, 0, 0, row[1], Persona.check(row[2], user.cont_per))
                return user.to_JSON()
        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def readxID(cls, db, id):
        try:
            cursor = db.cursor()
            sql = ("SELECT p.id_per, r.nomb_rol, p.nomb_per, "
                          "p.apel_per, p.dni_per, p.tele_per, "
                          "p.coun_per, p.corr_per "
                   "FROM Persona p " 
                   "INNER JOIN Rol R ON p.id_rol = r.id_rol "
                   "WHERE p.id_per = '{}';".format(id))
            
            cursor.execute(sql)
            row = cursor.fetchone()
            
            if row != None:
                user = Persona(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], None)
                return user
        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def read(cls, db):
        try:
            cursor = db.cursor()
            personas = []
            
            sql = ("SELECT p.id_per, r.nomb_rol, p.nomb_per, "
                          "p.apel_per, p.dni_per, p.tele_per, "
                          "p.coun_per, p.corr_per "
                   "FROM Persona p " 
                   "INNER JOIN Rol R ON p.id_rol = r.id_rol")
            cursor.execute(sql)
            
            resultset = cursor.fetchall()
            
            for row in resultset:
                persona = Persona(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "Inaccesible por hasheo")
                personas.append(persona.to_JSON())
            return personas
        except Exception as ex:
            raise Exception(ex)