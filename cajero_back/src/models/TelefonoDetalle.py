
class TelefonoDetalle:
    
    def __init__(self, id_adeudo, id_tarjeta=None, id_servicio=None, nombre=None, num_telefono=None, monto=None, meses=None, activo=None) -> None:
        self._id_adeudo = id_adeudo
        self._id_tarjeta = id_tarjeta
        self._id_servicio= id_servicio
        self._nombre = nombre
        self._num_telefono = num_telefono
        self._monto = float(monto) if monto is not None else None
        self._meses = meses
        self._actiivo = activo
        
    @property
    def id_adeudo(self):
        return self._id_adeudo
    
    @property
    def id_tarjeta(self):
        return self._id_tarjeta
    
    @property
    def id_servicio(self):
        return self._id_servicio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def num_telefono(self):
        return self._num_telefono
    
    @property
    def monto(self):
        return self._monto
    
    @property
    def meses(self):
        return self._meses
    
    @property
    def activo(self):
        return self._actiivo
    
    
    def to_JSON(self):
        return {
            'id_adeudo':self.id_adeudo,
            'id_tarjeta':self.id_tarjeta,
            'id_servicio':self.id_servicio,
            'nombre':self.nombre,
            'num_telefono':self.num_telefono,
            'monto':self.monto,
            'meses':self.meses,
            'activo':self.activo
        }
    
    