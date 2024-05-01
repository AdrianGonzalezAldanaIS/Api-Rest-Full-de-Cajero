
class PaggoServicio:
    
    def __init__(self, id_adeudo, monto_pago, id_tarjeta, id_servicio) -> None:
        self._id_adeudo = id_adeudo
        self._monto_pago = monto_pago
        self._id_tarjeta = id_tarjeta
        self._id_servicio = id_servicio
    
    @property
    def id_adeudo(self):
        return self._id_adeudo
    
    @property
    def monto_pago(self):
        return self._monto_pago
    
    @property
    def id_tarjeta(self):
        return self._id_tarjeta
    
    @property
    def id_servicio(self):
        return self._id_servicio
    
    def to_JSON(self):
        return {
            'id_adeudo':self.id_adeudo,
            'monto_pago':self.monto_pago,
            'id_tarjeta':self.id_tarjeta,
            'id_servicio':self.id_servicio
        }