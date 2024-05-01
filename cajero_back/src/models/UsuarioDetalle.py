class UsuariDetalle:
    
    def __init__(self, id_tarjeta, id_usuario=None, nombre='', saldo=None) -> None:
        self._id_tarjeta = id_tarjeta
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._saldo = float(saldo) if saldo is not None else None
    
    @property
    def id_tarjeta(self):
        return self._id_tarjeta
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def saldo(self):
        return self._saldo
    
    def to_JSON(self):
        return {
            'id_tarjeta':self.id_tarjeta,
            'id_usuario':self.id_usuario,
            'nombre':self.nombre,
            'saldo':self.saldo
        }