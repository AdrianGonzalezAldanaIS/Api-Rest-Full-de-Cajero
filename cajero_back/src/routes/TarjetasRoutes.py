from flask import Blueprint, request
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

@main.route('/retirar/<int:id>/', methods = ['POST'])
def retirar(id):
    cantidad = request.json.get('cantidad') # type: ignore
    return servicio_tarjeta.retirar(id, cantidad)

@main.route('/depositar/<int:id>/', methods = ['POST'] )
def depositar(id):
    cantidad = request.json.get('cantidad') # type: ignore
    return servicio_tarjeta.depositar(id, cantidad)


    