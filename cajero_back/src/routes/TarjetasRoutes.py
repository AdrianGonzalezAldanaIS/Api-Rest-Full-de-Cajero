from flask import Blueprint, jsonify
from dao.TarjetaDAO import TarjetaDao
from services.ServicioTarjeta import ServicioTarjeta

main = Blueprint('tarjeta_blueprint', __name__)
tarjeta_dao = TarjetaDao()
servicio_tarjeta = ServicioTarjeta(tarjeta_dao)



@main.route('/<int:id>')
def consulta_tarjeta(id):
    return servicio_tarjeta.consulta_tarjeta(id)

@main.route('/verificada/<int:id>', endpoint='cajero')
def verifica_tarjeta(id):
    return servicio_tarjeta.verifica_tarjeta(id)

@main.route('/fecha_verificada/<int:id>')
def verifica_fecha(id):
    return servicio_tarjeta.verifica_fecha(id)

@main.route('/bloqueada/<int:id>')
def verifica_bloqueo(id):
    return servicio_tarjeta.verifica_bloqueo(id)

@main.route('/nip/<int:id>/<int:nip>')
def verifica_nip(id, nip):
    return servicio_tarjeta.verifica_nip(id, nip)

@main.route('/saldo/<int:id>')
def consulta_saldo(id):
    return servicio_tarjeta.conslta_saldo(id)

@main.route('/limite/<int:id>')
def consulta_limite(id):
    return servicio_tarjeta.consulta_limite(id)

@main.route('/retirar/<int:id>/<int:cantidad>')
def retirar(id, cantidad):
    return servicio_tarjeta.retirar(id, cantidad)

@main.route('/depositar/<int:id>/<int:cantidad>')
def depositar(id, cantidad):
    return servicio_tarjeta.depositar(id, cantidad)




@main.route('/num_conexiones')
def get_num_conexiones():
    try:
        tarjeta = TarjetaDao.get_num_conexiones()
        
        return jsonify(tarjeta)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/')
def get_tarjetas():
    try:
        tarjetas = TarjetaDao.get_tarjetas()
        return jsonify(tarjetas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
"""
@main.route('/<id>')
def get_tarjeta(id):
    try:
        tarjeta = TarjetaDao.get_tarjeta_id(id)
        if tarjeta != None:
            return jsonify(tarjeta)
        else:
            return jsonify({}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
"""
@main.route('/saldo/<id>')
def get_saldo(id):
    try:
        tarjeta = TarjetaDao.get_tarjeta_saldo_id(id)
        if tarjeta != None:
            return jsonify(tarjeta)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
    
    