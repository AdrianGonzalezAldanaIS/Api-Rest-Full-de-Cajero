from interfaces.IPagoServicioTelefono import IPagoServicioTelefono
from  database.postgres_db import PostgresDB
from models.TelefonoDetalle import TelefonoDetalle
from models.Adeudo import Adeudo


pgdb = PostgresDB()

class PagosServicioTelefonoDAO(IPagoServicioTelefono):
    
    @classmethod
    def consulta_telefono(cls, id):
        es_adeudo = False
        if isinstance(id, int):
            
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT a.id_adeudo, t.id_tarjeta, s.id_servicio, u.nombres, u.num_telefono, a.activo FROM adeudos a, tarjetas t, servicios s, usuarios u WHERE t.id_tarjeta = a.id_tarjeta AND a.id_servicio = s.id_servicio AND t.id_usuario = u.id_usuario And a.id_tarjeta = %s And a.id_servicio = 'NET-IN'", (id,))
                    row1 = cursor.fetchone()
                    print("row",row1)
                    #hacer otro cursor con 
                    cursor.execute("SELECT sum(monto_adeudo) total, count(activo) meses FROM adeudos WHERE id_servicio = 'NET-IN' AND id_tarjeta = %s;",(id,))
                    row2 = cursor.fetchone()
                    
                    tel_detalle = TelefonoDetalle(id_adeudo=row1[0], id_tarjeta=row1[1], id_servicio=row1[2], nombre=row1[3], num_telefono=row1[4],monto=row2[0], meses=row2[1], activo=row1[5])
                    tel_detalle = tel_detalle.to_JSON()
                    print("tel detalle",tel_detalle)
            except Exception as ex:
                raise BaseException(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero")  
        return tel_detalle


    @classmethod
    def pago_telefono(cls, id):
        mensaje = ""
        filas_afectadas = 0
        if isinstance(id, int):
            datos_adeudo = cls.verifica_adeudo_telefono(cls, id)
            if len(datos_adeudo) != 0:
                print("Entro a datos_adeudos")
                try:
                    with pgdb.get_cursor() as cursor:
                        cursor.execute("INSERT INTO pagos_servicios(id_adeudo, fecha_pago, monto_pago, id_tarjeta, id_servicio) VALUES(%s, %s, %s, %s, %s);", (datos_adeudo['id_adeudo'],datos_adeudo['fecha_adeudo'],datos_adeudo['monto_adeudo'], datos_adeudo['id_tarjeta'], datos_adeudo['id_servicio']))
                        filas_afectadas = cursor.rowcount
                        mensaje = "Registro exitoso"
                        print("afectadas;", filas_afectadas)
                except Exception as ex:
                    raise BaseException(ex)
        else:
            raise BaseException("El tipo de dato debe ser un entero")  
        return filas_afectadas, mensaje
        
    def verifica_adeudo_telefono(self, id):
        if isinstance(id, int):
            try:
                with pgdb.get_cursor() as cursor:
                    cursor.execute("SELECT id_adeudo, id_servicio, id_tarjeta, fecha_adeudo, monto_adeudo, activo FROM adeudos WHERE id_tarjeta = %s AND id_servicio = 'NET-IN';", (id,))
                    row = cursor.fetchone()
                    adeudos = Adeudo(id_adeudo=row[0], id_servicio=row[1], id_tarjeta=row[2], fecha_adeudo=row[3], monto_adeudo=row[4], activo=row[5])
                    adeudos = adeudos.to_JSON()
            except Exception as ex:
                raise BaseException(ex) 
        else:
            raise BaseException("El tipo de dato debe ser un entero")  
        return adeudos
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    