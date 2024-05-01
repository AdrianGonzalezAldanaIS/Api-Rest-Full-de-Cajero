import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        conn =  psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
        return conn
    except DatabaseError as ex:
        print("Error en la conexion")