
from .cliente_consumo import Cliente_cosnumo
class ClienteServicio():
    cliente = Cliente_cosnumo()

    """
    Clase que implementa la interfaz ClienteInterfaz, esto con el fin de reducir el acoplamiento.
    Clase encargada de hacer las validaciones pertinentes sobre las respuestas del servidor
    """

    def valida_terjeta(self, num_tarjet):
        respuesta = {"mensaje": "La tarjeta se encuentra dentro de las validaciones requeridas","verificada":True}
        if not self.cliente.consulta_tarjeta(num_tarjet):
            respuesta['mensaje'] = 'El numero de la tarjeta no esta registrada'
            respuesta['verificada'] = False
            return respuesta
        elif not self.cliente.consulta_verificada(num_tarjet):
            respuesta['mensaje'] = 'La tarjeta no esta verificada'
            respuesta['verificada'] = False
            return respuesta
        elif not self.cliente.consulta_vencida(num_tarjet):
            respuesta['mensaje'] = 'La tarjeta expiro'
            respuesta['verificada'] = False
            return respuesta
        elif self.cliente.consulta_bloqueada(num_tarjet):
            respuesta['mensaje'] = 'La tarjeta esta bloqueada'
            respuesta['verificada'] = False
            return respuesta
       
        return respuesta