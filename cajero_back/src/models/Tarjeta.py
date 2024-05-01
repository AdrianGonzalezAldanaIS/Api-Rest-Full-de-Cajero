from utils.Dateformat import Dateformat

class Tarjeta:
    def __init__(self, id_tarjeta, fecha_verificada=None, nip=None, intentos=None, saldo=None, limite=None, bloqueada=None, verificada=None, id_usuario=None) -> None:
        self._id_tarjeta = id_tarjeta
        self._fecha_verificada = Dateformat.conver_to_date(fecha_verificada)
        self._nip = nip
        self._intentos = intentos
        self._saldo = float(saldo) if saldo is not None else None
        self._limite = float(limite) if limite is not None else None
        self._bloqueada = bloqueada
        self._verificada = verificada
        self._id_usuario = id_usuario
    
    
    @property
    def id_tar(self):
        return self._id_tarjeta
    
    @property
    def fech_ver(self):
        return self._fecha_verificada
    
    @property
    def nip(self):
        return self._nip
    
    @property
    def num_intentos(self):
        return self._intentos
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def lim(self):
        return self._limite
    
    @property
    def bloqueada(self):
        return self._bloqueada
    
    @property
    def verificada(self):
        return self._verificada
    
    @property
    def usuario(self):
        return self._id_usuario
    
    def to_JSON(self):
        """
        Returns:
            _type_: _description_
        """
        return {
            'id_tarjeta':self.id_tar,
            'fecha_verificada':self.fech_ver,
            'nip':self.nip,
            'intentos':self.num_intentos,
            'saldo':self.saldo,
            'limite':self.lim,
            'bloqueada':self.bloqueada,
            'verificada':self.verificada,
            'id_usuario':self.usuario
        }