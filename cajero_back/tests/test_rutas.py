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
    #print("creando cliente...")
    return app.test_client()


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
        assert response.status_code == 404
        assert response.json == {"Estatus": False}
    
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
        assert response.status_code == 404
        assert response.json == {"Estatus": True}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        