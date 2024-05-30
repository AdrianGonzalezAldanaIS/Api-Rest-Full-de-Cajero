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
    
    def consulta_nip(self, id_tarjeta, nip):
        url_nip = f"http://localhost:4000/api/tarjetas/nip/{id_tarjeta}/{nip}"
        resp = requests.get(url_nip)
        data = json.loads(resp.content)
        return data
    
    def consulta_saldo(self, id_tarjeta):
        url_saldo = f"http://localhost:4000/api/tarjetas/saldo/{id_tarjeta}"
        resp = requests.get(url_saldo)
        data = json.loads(resp.content)
        return data
    
    
    def consulta_limite(self, id_tarjeta):
        url_limite = f"http://localhost:4000/api/tarjetas/limite/{id_tarjeta}"
        resp = requests.get(url_limite)
        data = json.loads(resp.content)
        return data
    
    def retirar(self, id_tarjeta, cantidad):
        print("YYYCantidad",cantidad)
        url_actualiza = f"http://localhost:4000/api/tarjetas/retirar/{id_tarjeta}"
        response = requests.post(url_actualiza, json={'cantidad': cantidad})
        data = response.json()
        return data
    
    def depositar(self, id_tarjeta, cantidad):
        print("XXXCantidadXXX",cantidad)
        url_actualiza = f"http://localhost:4000/api/tarjetas/depositar/{id_tarjeta}"
        response = requests.post(url_actualiza, json={'cantidad': cantidad})
        data = response.json()
        print("DDATAAAA",data)
        return data

