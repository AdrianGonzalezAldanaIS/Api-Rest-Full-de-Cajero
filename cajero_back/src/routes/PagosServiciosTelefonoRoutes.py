from flask import Blueprint
from flask_restx import Api, Resource
from dao.PagoServicioTelefonoDAO import PagosServicioTelefonoDAO
from services.ServicioPagosServicios import ServicioPagoServicios


main = Blueprint('pago_servicios_blueprint', __name__)
api = Api(main, version="1.0", title="Api", description="End points")
tarjeta_dao = PagosServicioTelefonoDAO()
servicio_tarjeta = ServicioPagoServicios(tarjeta_dao)

@api.route('/telefono/<int:id>')
class ConsultaTelefono(Resource):
    def get(self, id):
        return servicio_tarjeta.consulta_telefono(id)

@api.route('/telefono/servicio/<int:id>')
class PagoTelefono(Resource):
    def get(self, id):
        return servicio_tarjeta.pago_telefono(id)

