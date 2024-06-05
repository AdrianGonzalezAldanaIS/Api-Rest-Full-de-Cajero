
from interfaces.ITarjeta import ITarjeta
from models.Tarjeta import Tarjeta
from models.UsuarioDetalle import UsuariDetalle
import datetime
from  database.postgres_db import PostgresDB

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
                    if row is not None:
                        tarjeta = Tarjeta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                        tarjeta = tarjeta.to_JSON()
                    else :
                        tarjeta = None 
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
                    if row is not None:
                        tarjeta = Tarjeta(id_tarjeta=row[0], verificada=row[1], fecha_verificada=row[2])
                        tarjeta = tarjeta.to_JSON()
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
                    else:
                        tarjeta = None
            except Exception as ex:
                print(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
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
                        cursor.execute("UPDATE tarjetas SET intentos = 0, bloqueada = false WHERE id_tarjeta = %s;", (id,))
                        filas_afectadas = cursor.rowcount
                    else:
                        cursor.execute("UPDATE tarjetas SET intentos = intentos + 1 WHERE id_tarjeta = %s;", (id,))
                        es_valida = False
                        filas_afectadas = cursor.rowcount
                        
                    cursor.execute("SELECT id_tarjeta, intentos, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    tarjeta = Tarjeta(id_tarjeta=row[0], intentos=row[1], fecha_verificada=row[2])
                    tarjeta = tarjeta.to_JSON()
                    if tarjeta['intentos'] > 3:
                        cursor.execute("UPDATE tarjetas SET bloqueada = true WHERE id_tarjeta = %s;", (id,))
                        filas_afectadas = cursor.rowcount
                        es_valida = False
            except Exception as ex:
                raise BaseException(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
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
                    else:
                        us_detalle = False
            except Exception as ex:
                raise BaseException(ex) 
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
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
                    else:
                        tarjeta = False
            except Exception as ex:
                print(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero") 
        return tarjeta
    
    @classmethod
    def retirar(cls, id, cantidad):
        filas_afectadas = 0
        flag = False
        mensaje = ""
        flag, mensaje = cls.validar_cantidad(id, cantidad)  # type: ignore
        if isinstance(id, int) and id >= 0 and isinstance(cantidad, float) and cantidad >= 0.0:
            if flag:
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
        return filas_afectadas, mensaje, flag
    
    @classmethod
    def validar_cantidad(cls, id, cantidad):
        flag = False
        if cantidad > 0.0:
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_tarjeta, limite, saldo, fecha_verificada FROM tarjetas WHERE id_tarjeta = %s;", (id,))
                    row = cursor.fetchone()
                    tarjeta = Tarjeta(id_tarjeta=row[0], limite=row[1], saldo=row[2], fecha_verificada=row[3])
                    tarjeta = tarjeta.to_JSON()
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
        return flag, mensaje
    
    @classmethod
    def depositar(cls, id, cantidad): 
        filas_afectadas = 0
        mensaje = ""
        if isinstance(id, int) and id >= 0:
            if isinstance(cantidad, float) and cantidad > 0:
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
