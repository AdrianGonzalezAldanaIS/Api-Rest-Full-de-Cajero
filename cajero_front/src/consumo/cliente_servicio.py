
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
            respuesta['mensaje'] = 'La tarjeta expiró'
            respuesta['verificada'] = False
            return respuesta
        elif self.cliente.consulta_bloqueada(num_tarjet):
            respuesta['mensaje'] = 'La tarjeta esta bloqueada'
            respuesta['verificada'] = False
            return respuesta
       
        return respuesta

    def validate_nip(self, num_tarjeta, nip):
        pasa = self.cliente.consulta_nip(num_tarjeta, nip)
        respuesta = {"mensaje": "El NIP es correcto","verificada":True, "intentos":pasa['intentos']}
        if not pasa["Estatus"]:
            respuesta['mensaje'] = "Lo sentimos, tu NIP es incorrecto 🧐"
            respuesta['verificada'] = pasa['Estatus']
            respuesta["intentos"] = pasa['intentos']
        return respuesta

    def verifica_saldo(self, num_tarjeta):
        return self.cliente.consulta_saldo(num_tarjeta)

    def verifica_limite(self, num_tarjeta):
        return self.cliente.consulta_limite(num_tarjeta)
    
    def realiza_retiro(self,id_tarjeta,cantidad):
        saldo = self.cliente.consulta_saldo(id_tarjeta)
        data = self.cliente.retirar(id_tarjeta, cantidad)
        respuesta  = {"mensaje":"Retiro exitoso","retiro":True,"saldo":saldo['saldo']}
        if data['filas_afectadas'] == 0:
            respuesta["mensaje"] = data['Mensaje']
            respuesta["retiro"] = data['retiro_valido']
        return respuesta
    
    def realizar_deposito(self, id_tarjeta, cantidad):
        saldo = self.cliente.consulta_saldo(id_tarjeta)
        data = self.cliente.depositar(id_tarjeta, cantidad)
        respuesta  = {"mensaje":"Deposito exitoso","deposito":True,"saldo":saldo['saldo']}
        if data['filas_afectadas'] == 0:
            respuesta["mensaje"] = data['Mensaje']
        return respuesta