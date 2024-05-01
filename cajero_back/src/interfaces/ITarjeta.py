from abc import abstractmethod
from abc import ABCMeta

class ITarjeta(metaclass=ABCMeta):
    
    @abstractmethod
    def consulta_tarjeta(cls, id):
        pass
    @abstractmethod
    def verifica_tarjeta(cls, id):
        pass
    @abstractmethod
    def verifica_fecha(cls, id):
        pass
    @abstractmethod
    def verifica_bloqueo(cls, id):
        pass
    
    @abstractmethod
    def verifica_nip(cls, id, nip):
        pass

    @abstractmethod
    def consulta_saldo(cls, id):
        pass

    @abstractmethod   
    def consulta_limite(self, id):
        pass
    
    @abstractmethod
    def retirar(cls, id, cantidad):
        pass
    
    @abstractmethod
    def depositar(cls, id, cantidad):
        pass