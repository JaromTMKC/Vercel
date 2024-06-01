import pyodbc

class Config():
    SECRET_KEY = "Valentino71722012."

class DevelopmentConfig(Config):
    HOST = "fiisiav.cd2q4kywcppm.us-east-2.rds.amazonaws.com,1433"
    USER = "JaromTMKA"
    PASSWORD = "Vale71722012."
    DB = "FIISI - AV"

    @staticmethod
    def conection():
        try:
            conexion = pyodbc.connect(
                'DRIVER={SQL Server};'
                f'SERVER={DevelopmentConfig.HOST};'
                f'DATABASE={DevelopmentConfig.DB};'
                f'UID={DevelopmentConfig.USER};'
                f'PWD={DevelopmentConfig.PASSWORD};'
                'CHARSET=UTF8;'
            )
            return conexion
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print("Error de conexion a la base de datos:", sqlstate)