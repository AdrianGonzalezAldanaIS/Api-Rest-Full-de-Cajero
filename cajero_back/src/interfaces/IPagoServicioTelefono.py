from abc import abstractmethod
from abc import ABCMeta

class IPagoServicioTelefono(metaclass=ABCMeta):
    

    @abstractmethod
    def consulta_telefono(cls, id):
        pass
    
    @abstractmethod
    def pago_telefono(cls, id):
        pass