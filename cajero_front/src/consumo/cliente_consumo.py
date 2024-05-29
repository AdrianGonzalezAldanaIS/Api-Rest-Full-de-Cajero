import requests 
import json

class Cliente_cosnumo:
    
    def consulta_tarjeta(self, id_tarjeta):
        url = f'http://localhost:4000/api/tarjetas/{id_tarjeta}'
        res = requests.get(url)
        data = json.loads(res.content)
        return data['Estatus']
    
    def consulta_verificada(self, id_tarjeta):
        url_verificada = f"http://localhost:4000/api/tarjetas/verificada/{id_tarjeta}"
        resp = requests.get(url_verificada)
        data = json.loads(resp.content)
        return data['Estatus']
    

    def consulta_vencida(self, id_tarjeta):
        url_vencida = f"http://localhost:4000/api/tarjetas/fecha_verificada/{id_tarjeta}"
        resp = requests.get(url_vencida)
        data = json.loads(resp.content)
        return data['Estatus']
    
    def consulta_bloqueada(self, id_tarjeta):
        url_bloqueada = f"http://localhost:4000/api/tarjetas/bloqueada/{id_tarjeta}"
        resp = requests.get(url_bloqueada)
        data = json.loads(resp.content)
        print("dataaaa ", data)
        return data['Estatus']
    
    def consulta_nip(self, num_tarjeta, nip):
        url_nip = "http://localhost:4000/nip/"
        resp = requests.get(url_nip + num_tarjeta+"/"+nip)
        data = json.loads(resp.content)
        return data
    
    def consulta_saldo(self, num_tarjeta):
        url_saldo = "http://localhost:4000/retiro/saldo/"
        resp = requests.get(url_saldo + num_tarjeta)
        data = json.loads(resp.content)
        return data['mensaje_alert']
    
    
    def consulta_limite(self, num_tarjeta):
        url_limite = "http://localhost:4000/retiro/limite/"
        resp = requests.get(url_limite + num_tarjeta)
        data = json.loads(resp.content)
        return data['mensaje_alert']

    def verifica_saldo(self,num_tarjeta,cantidad):
        url_verifica_saldo = "http://localhost:4000/retira/saldo/"
        resp = requests.get(url_verifica_saldo + num_tarjeta+"/"+str(cantidad))
        data = json.loads(resp.content)
        return data['mensaje_alert']
    
    def verifica_limite(self, num_tarjeta,cantidad):
        url_verifica_limite = "http://localhost:4000/retira/limite/"
        resp = requests.get(url_verifica_limite + num_tarjeta+"/"+str(cantidad))
        data = json.loads(resp.content)
        return data['mensaje_alert']
    
    
