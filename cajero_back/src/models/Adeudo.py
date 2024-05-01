from utils.Dateformat import Dateformat

class Adeudo:
    
    def __init__(self, id_adeudo, id_servicio=None, id_tarjeta=0, fecha_adeudo=None, monto_adeudo=None, activo=None) -> None:
        self._adeudo = id_adeudo
        self._servicio = id_servicio
        self._tarjeta = id_tarjeta
        self._fecha = Dateformat.conver_to_date(fecha_adeudo)
        self._monto = float(monto_adeudo) if monto_adeudo is not None else None
        self._is_activo = activo
        
    @property
    def id_adeudo(self):
        return self._adeudo
    
    @property
    def id_servicio(self):
        return self._servicio
    
    @property
    def id_tarjeta(self):
        return self._tarjeta
    
    @property
    def fecha_adeudo(self):
        return self._fecha
    
    @property
    def monto_adeudo(self):
        return self._monto
    
    @property
    def is_activo(self):
        return self._is_activo
    
    def to_JSON(self):
        return {
            "id_adeudo":self.id_adeudo,
            "id_servicio":self.id_servicio,
            "id_tarjeta":self.id_tarjeta,
            "fecha_adeudo":self.fecha_adeudo,
            "monto_adeudo":self.monto_adeudo,
            "is_activo":self.is_activo
        }
        
        
    