from interfaces.ITarjeta import ITarjeta
from flask import jsonify

class ServicioTarjeta:
    
    def __init__(self, i_tarjeta: ITarjeta) -> None:
        self.i_tarjeta = i_tarjeta
    
    def consulta_tarjeta(self, id):
        try:
            tarjeta = self.i_tarjeta.consulta_tarjeta(id)
            if tarjeta != None:
                return jsonify({"Estatus":True})
            else:
                return jsonify({"Estatus":False}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}),500

    def verifica_tarjeta(self, id):
        try:
            tarjeta = self.i_tarjeta.verifica_tarjeta(id)
            if tarjeta != None:
                print("TARJETAAAA",tarjeta['verificada'])
                return jsonify({"Estatus":True})
            else:
                return jsonify({"Estatus":False}), 404
        except Exception as ex:
            return jsonify({'messageSSSSS': str(ex)}),500
    
    def verifica_fecha(self, id):
        print("entro a la func")
        try:
            print("Entro a fecha verificada")
            tarjeta = self.i_tarjeta.verifica_fecha(id)
            print("veri",tarjeta)
            if tarjeta == True:
                return jsonify({"Estatus":tarjeta})
            else:
                return jsonify({"Estatus":tarjeta}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}),500
    
    def verifica_bloqueo(self, id):
        try:
            tarjeta = self.i_tarjeta.verifica_bloqueo(id)
            if tarjeta != None:
                print("TARJETAAAA",tarjeta['bloqueada'])
                return jsonify({"Estatus":False})
            else:
                return jsonify({"Estatus":True}), 404
        except Exception as ex:
            return jsonify({'messageSSSSS': str(ex)}),500
        
    def verifica_nip(self, id, nip):
        try:
            row = self.i_tarjeta.verifica_nip(id, nip)
            print("nip---",row)
            if row != None:
                return jsonify({"Estatus":row[0], "afecto":row[1]})
            else:
                return jsonify({"Estatus":row[0], "afecto":row[1]}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}),500

    def conslta_saldo(self, id):
        try:
            tarjeta = self.i_tarjeta.consulta_saldo(id)
            print("id_tarjeta---",tarjeta)
            if len(tarjeta) != 0:
                return jsonify({"id_tarjeta":tarjeta['id_tarjeta'], "id_usuario":tarjeta['id_usuario'],"nombre":tarjeta['nombre'], "saldo":tarjeta['saldo']})
            else:
                return jsonify({"id_tarjeta":tarjeta['id_tarjeta'], "id_usuario":tarjeta['id_usuario'],"nombre":tarjeta['nombre'], "saldo":tarjeta['saldo']}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}),500

    def consulta_limite(self, id):
        try:
            limite = self.i_tarjeta.consulta_limite(id)
            print("limite",limite)
            if len(limite) != 0:
                return jsonify({"Estatus":limite['limite']})
            else:
                return jsonify({"Estatus":limite['limite']}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}),500

    def retirar(self, id, cantidad):
        try:
            filas_afectadas, mensaje = self.i_tarjeta.retirar(id, cantidad)
            print("filas:", filas_afectadas)
            print("mensaje:", mensaje)
            if filas_afectadas != 0:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
            else:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
        except Exception as ex:
            return jsonify({'message': str(ex)}),500
"""
    def depositar(self, id, cantidad):
        try:
            filas_afectadas, mensaje = self.i_tarjeta.depositar(id, cantidad)
            if filas_afectadas != 0:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
            else:
                return jsonify({"Mensaje":mensaje,"filas_afectadas":filas_afectadas})
        except Exception as ex:
            return jsonify({'message': str(ex)}),500

"""