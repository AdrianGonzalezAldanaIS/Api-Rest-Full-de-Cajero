from database.db import get_connection
from singleton.SingletoBaseDatosConn import SingletoBaseDatosConn

class ManejadorBaseDatos(metaclass=SingletoBaseDatosConn):
    connection = None

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            #print("Nueva instancia1")
            cls.connection = get_connection()
        return cls.connection