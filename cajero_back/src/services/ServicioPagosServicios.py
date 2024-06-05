from interfaces.IPagoServicioTelefono import IPagoServicioTelefono
from flask import jsonify

class ServicioPagoServicios:
    
    def __init__(self, i_tarjeta: IPagoServicioTelefono) -> None:
        self.i_tarjeta = i_tarjeta
    
    def consulta_telefono(self, id):
        try:
            row = self.i_tarjeta.consulta_telefono(id)
            if len(row) != 0: # type: ignore
                return jsonify(row)
            else:
                print("1")
                return jsonify({"Estatus":False}), 404
        except Exception as ex:
            print("2")
            return jsonify({'message': str(ex)}),500
        
    def pago_telefono(self, id):
        try:
            filas_afectadas, mensaje = self.i_tarjeta.pago_telefono(id) # type: ignore
            print("filas:", filas_afectadas)
            print("mensaje:", mensaje)
            if filas_afectadas != 0:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
            else:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
        except Exception as ex:
            return jsonify({'message': str(ex)}),500
    
    
    