import pytest
from src.app import create_app
from src.database.postgres_db import PostgresDB

@pytest.fixture(scope="session")
def app():
    # Setup de la apliacción 
    app = create_app()
    
    # Modo test para capturar las excepciones que lanza el servidor
    app.config.update({
        "TESTING": True,
    })

    # Inicialización de la base de datos
    pgdb = PostgresDB()
    pgdb.init_app(app)
    yield app
    # apartir de aquí se pone el código para liberar los recursos 

    # teardown limpiar/ reinicializar

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()

@pytest.fixture
def envio_peticion(client):
    def _envio_peticion():
        return client.get("api/tarjetas/nip/1021/8119")
    return _envio_peticion

def test_consulta_tarjeta_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/1000")
        assert response.status_code == 200
        assert response.json == {"Estatus": True}
        
def test_consulta_tarjeta_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/999")
        assert response.status_code == 404
        assert response.json == {"Estatus": False}
        
def test_verifica_tarjeta_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/verificada/1000")
        assert response.status_code == 200
        assert response.json == {"Estatus": True}
        
def test_verifica_tarjeta_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/verificada/999")
        assert response.status_code == 500
        assert response.json == {"Estatus": "'NoneType' object is not subscriptable"}
    
def test_verifica_fecha_tarjeta_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/fecha_verificada/1000")
        assert response.status_code == 200
        assert response.json == {"Estatus": True}
        
def test_verifica_fecha_tarjeta_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/fecha_verificada/999")
        assert response.status_code == 404
        assert response.json == {"Estatus": False}
    

def test_verifica_bloqueo_tarjeta_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/bloqueada/1000")
        assert response.status_code == 200
        assert response.json == {"Estatus": False}
        
def test_verifica_bloqueo_tarjeta_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/bloqueada/999")
        assert response.status_code == 500
        assert response.json == {"messageSSSSS": "'NoneType' object is not subscriptable"}
        
def test_verifica_nip_id_no_valido(app, envio_peticion):
    for x in range(4):
        response = envio_peticion()
        assert response.status_code == 404
        assert response.json == {"Estatus": False, "afecto": 1, "intentos": x+1}
        
def test_verifica_nip_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/nip/1021/8112")
        assert response.status_code == 200
        assert response.json == {"Estatus": True,"afecto": 1,"intentos": 0}

def test_consulta_saldo_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/saldo/1000")
        assert response.status_code == 200
        assert response.json == {"id_tarjeta": 1000,"id_usuario": 75,"nombre": "Winnie","saldo": 57450.0}

def test_consulta_saldo_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/saldo/999")
        assert response.status_code == 404
        assert response.json == {"Estatus": False}

def test_consulta_limite_id_valido(app, client):
    with client:
        response = client.get("api/tarjetas/limite/1000")
        assert response.status_code == 200
        assert response.json == {"limite": 10000.0}

def test_consulta_limite_id_invalido(app, client):
    with client:
        response = client.get("api/tarjetas/limite/999")
        assert response.status_code == 404
        assert response.json == {"limite": False}

def test_retirar_id_valido(app, client):
    with client:
        data = {"cantidad": 10.0}
        response = client.post("api/tarjetas/retirar/1021/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje": "Cantidad aceptada",
  "filas_afectadas": 1,"retiro_valido":True}

def test_retirar_saldo_cero(app, client):
    with client:
        data = {"cantidad": 0.0}
        response = client.post("api/tarjetas/retirar/1021/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje": "La cantidad debe ser mayo a $0.00",
  "filas_afectadas": 0,"retiro_valido":False}

def test_retirar_saldo_cantidad_mayor_al_limite(app, client):
    with client:
        data = {"cantidad": 11000.0}
        response = client.post("api/tarjetas/retirar/1021/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje": "Cantidad mayor al limite",
  "filas_afectadas": 0,"retiro_valido":False}

def test_retirar_saldo_cantidad_insuficiente(app, client):
    with client:
        data = {"cantidad": 9000.0}
        response = client.post("api/tarjetas/retirar/1040/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje": "Cantidad insuficiente",
  "filas_afectadas": 0,"retiro_valido":False}

def test_depositar_cantidad_valida(app, client):
    with client:
        data = {"cantidad": 100.0}
        response = client.post("api/tarjetas/depositar/1040/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje":'Depsoito exitoso',"filas_afectadas":1}

def test_depositar_cantidad_cero(app, client):
    with client:
        data = {"cantidad": 0.0}
        response = client.post("api/tarjetas/depositar/1040/", json=data)
        assert response.status_code == 200
        assert response.json == {"Mensaje":'Cantidad no valida',"filas_afectadas":0}
   
        
        