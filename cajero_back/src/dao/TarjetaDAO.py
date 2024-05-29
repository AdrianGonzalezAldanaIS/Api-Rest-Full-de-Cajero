
from interfaces.ITarjeta import ITarjeta
from models.Tarjeta import Tarjeta
from models.UsuarioDetalle import UsuariDetalle
import datetime
from  database.postgres_db import PostgresDB
#from exceptions.TipoDatoException import TipoDatoException

pgdb = PostgresDB()
class TarjetaDao(ITarjeta):
    """
        Operaciones de transacción de una tarjeta de debito
    """
    @classmethod
    def consulta_tarjeta(cls, id):
        tarjeta = None
        if isinstance(id, int):
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT * FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    print("row1111: ", row)
                    if row is not None:
                        tarjeta = Tarjeta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                        tarjeta = tarjeta.to_JSON()
                        print("tarjeta: ", tarjeta)
                    else :
                        tarjeta = None 
                """    
                connection2 = ManejadorBaseDatos.get_connection()
                with connection2.cursor() as cursor:
                    cursor.execute("SELECT * FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row2 = cursor.fetchone()
                    print("row: ", row2)
                """
            except Exception as ex:
                raise BaseException(ex) 
        else:
            raise BaseException("El tipo de dato debe ser un entero")  
        return tarjeta
    
    @classmethod
    def verifica_tarjeta(cls, id):
        trjeta = None
        if isinstance(id, int) and id >= 0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, verificada, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    print("row: ", row)
                    print("row:zzzzzzzzzzzzzzzzzzzzz ")
                    if row is not None:
                        tarjeta = Tarjeta(id_tarjeta=row[0], verificada=row[1], fecha_verificada=row[2])
                        tarjeta = tarjeta.to_JSON()
                        print("tarjeta: ", tarjeta)
                    else:
                        tarjeta = None
            except Exception as ex:
                raise BaseException(ex) 
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
        return tarjeta
    
    @classmethod
    def verifica_fecha(cls, id):
        fecha_verificada = False
        if isinstance(id, int) and id >= 0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    
                    if datetime.date.today() < row[0]:
                        fecha_verificada = True
                    else:
                        fecha_verificada = False
            except Exception as ex:
                print(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
        return fecha_verificada
    
    @classmethod
    def verifica_bloqueo(cls, id):
        tarjeta = None
        if isinstance(id, int) and id >= 0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, bloqueada, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    if row is not None:
                        tarjeta = Tarjeta(id_tarjeta=row[0], bloqueada=row[1], fecha_verificada=row[2])
                        tarjeta = tarjeta.to_JSON()
                        print("tar", tarjeta)
                    else:
                        tarjeta = None
            except Exception as ex:
                print(ex)
        else:
            print("entro a la excepcion")
            raise BaseException("El tipo de dato debe ser un entero") 
        print("bloqueada:",row)
        return tarjeta
        
    @classmethod
    def verifica_nip(cls, id, nip):
        es_valida = True
        filas_afectadas = 0
        if isinstance(id, int) and id >= 0 and isinstance(nip, int) and nip >= 0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, nip, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    tarjeta = Tarjeta(id_tarjeta=row[0], nip=row[1], fecha_verificada=row[2])
                    tarjeta = tarjeta.to_JSON()
                    if tarjeta['nip'] == nip:
                        print("Entro al nipppppp")
                        cursor.execute("UPDATE tarjetas SET intentos = 0, bloqueada = false WHERE id_tarjeta = %s;", (id,))
                        filas_afectadas = cursor.rowcount
                        print(filas_afectadas)
                    else:
                        print("entro al else")
                        cursor.execute("UPDATE tarjetas SET intentos = intentos + 1 WHERE id_tarjeta = %s;", (id,))
                        es_valida = False
                        filas_afectadas = cursor.rowcount
                        
                    cursor.execute("SELECT id_tarjeta, intentos, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    print("paso el cursor")
                    row = cursor.fetchone()
                    tarjeta = Tarjeta(id_tarjeta=row[0], intentos=row[1], fecha_verificada=row[2])
                    tarjeta = tarjeta.to_JSON()
                    if tarjeta['intentos'] > 3:
                        print("entro a más de 3")
                        cursor.execute("UPDATE tarjetas SET bloqueada = true WHERE id_tarjeta = %s;", (id,))
                        filas_afectadas = cursor.rowcount
                        es_valida = False
            except Exception as ex:
                raise BaseException(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
        print("Res", es_valida, filas_afectadas)
        return es_valida, filas_afectadas, tarjeta['intentos']
    
    @classmethod
    def consulta_saldo(cls, id):
        us_detalle = None
        if isinstance(id, int):
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT t.id_tarjeta, u.id_usuario, u.nombres, t.saldo FROM tarjetas t, usuarios u WHERE t.id_usuario = u.id_usuario AND t.id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    if row is not None:
                        us_detalle = UsuariDetalle(row[0], row[1], row[2], row[3])
                        us_detalle = us_detalle.to_JSON()
                        print("consulta saldo ",us_detalle)
                    else:
                        us_detalle = False
            except Exception as ex:
                raise BaseException(ex) 
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
        print(us_detalle) 
        return us_detalle
    
    @classmethod
    def consulta_limite(cls, id):
        tarjeta = None
        if isinstance(id, int) and id >= 0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, limite, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    if row is not None:
                        tarjeta = Tarjeta(id_tarjeta=row[0], limite=row[1], fecha_verificada=row[2])
                        tarjeta = tarjeta.to_JSON()
                        print("tar", tarjeta)
                    else:
                        tarjeta = False
            except Exception as ex:
                print(ex)
        else:
            print("entro a la excepcion")
            raise BaseException("El tipo de dato debe ser un entero") 
        print("bloqueada:",row)
        return tarjeta
    
    @classmethod
    def retirar(cls, id, cantidad):
        print("ID",id)
        print("SSSSCantidad",cantidad)
        filas_afectadas = 0
        flag = False
        mensaje = ""
        flag, mensaje = cls.validar_cantidad(id, cantidad)  # type: ignore
        if isinstance(id, int) and id >= 0 and isinstance(cantidad, float) and cantidad >= 0.0:
            print("Entro1")
            
            print("FLAAAAG",flag)
            print("MENSAJEE",mensaje)
            if flag:
                print("Entro2")
                try:
                    with pgdb.get_cursor() as cursor:
                        cursor.execute("UPDATE tarjetas SET saldo = saldo - %s WHERE id_tarjeta = %s;", (cantidad,id))
                        filas_afectadas = cursor.rowcount
                except Exception as ex:
                    print(ex)
            else:
                return filas_afectadas, mensaje, flag
        else:
            return filas_afectadas, mensaje, flag
        print("filas afectadas:",filas_afectadas)
        return filas_afectadas, mensaje, flag
    
    @classmethod
    def validar_cantidad(cls, id, cantidad):
        print("Entro3")
        print("IDbb",id)
        print("SSSSbbbbCantidad",cantidad)
        flag = False
        if cantidad > 0.0:
            try:
                print("Entro al try")
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, limite, saldo, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    tarjeta = Tarjeta(id_tarjeta=row[0], limite=row[1], saldo=row[2], fecha_verificada=row[3])
                    tarjeta = tarjeta.to_JSON()
                    print("tarzzzzz", tarjeta)
                    if cantidad <= tarjeta['limite']:
                        flag = True
                        mensaje = "Cantidad dentro del limite"
                        if cantidad <= tarjeta['saldo']:
                            flag = True
                            mensaje = "Cantidad aceptada"
                        else:
                            flag = False
                            mensaje = "Cantidad insuficiente"
                    else:
                        flag = False
                        mensaje = "Cantidad mayor al limite"
            except Exception as ex:
                print(ex)
        else:
            flag = False
            mensaje = "La cantidad debe ser mayo a $0.00"
        print("FLAAAAG222",flag)
        print("MENSAJEE222222",mensaje)
        return flag, mensaje
    
    
"""    
    @classmethod
    def depositar(cls, id, cantidad): 
        filas_afectadas = 0
        mensaje = ""
        if isinstance(id, int) and id >= 0:
            if isinstance(cantidad, int) and cantidad > 0:
                try:
                    with pgdb.get_cursor() as cursor:
                        cursor.execute("UPDATE tarjetas SET saldo = saldo + %s WHERE id_tarjeta = %s;", (cantidad,id))
                        filas_afectadas = cursor.rowcount
                        mensaje = "Depsoito exitoso"
                except Exception as ex:
                    print(ex)
            else:
                mensaje = "Cantidad no valida"
        return filas_afectadas, mensaje
"""
    
    
    
    
    
    
    
    
    
    
    
    
""" 
        
    @classmethod
    def get_tarjetas(cls):
        try:
            #connection = ManejadorBaseDatos.get_connection()
            print(connection)
            tarjetas_lis = []
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM tarjetas ORDER BY id_tarjeta ASC LIMIT 10;")
                resulset = cursor.fetchall()
                for row in resulset:
                    tarjeta = Tarjeta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    tarjetas_lis.append(tarjeta.to_JSON())
            return tarjetas_lis
        except Exception as ex:
            raise Exception("Error......",ex)
        
    @classmethod
    def get_tarjeta_id(cls, id):
        try:
            connection = ManejadorBaseDatos.get_connection()
            print(connection)
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                row = cursor.fetchone()
                print(row)
                tarjeta = None
                if row != None:
                    tarjeta = Tarjeta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    tarjeta = tarjeta.to_JSON()
            return tarjeta
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_tarjeta_saldo_id(cls, id):
        try:
            connection = ManejadorBaseDatos.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_tarjeta, saldo FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                id_tarjeta, saldo = cursor.fetchone()
                print(id_tarjeta, saldo)
                if id_tarjeta != None:
                    saldo = {'id_atrjeta':id_tarjeta
                             ,'saldo':saldo}
                else:
                    raise BdException("La consulta esta vacia")
            return saldo
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_num_conexiones(cls):

        try:
            connection = ManejadorBaseDatos.get_connection()
            with connection.cursor() as cursor:
            
                # Consulta para obtener el número de conexiones activas
                cursor.execute("SELECT count(*) FROM pg_stat_activity WHERE datname = current_database();")
                num_conexiones = cursor.fetchone()[0]
            return num_conexiones
        except Exception as ex:
            return -1
"""