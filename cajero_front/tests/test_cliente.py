import pytest
from src.app import create_app
from config import config

@pytest.fixture(scope="session")
def app():
    # Setup de la apliacción 

    app = create_app()
    
    # Modo test para capturar las excepciones que lanza el servidor
    app.config.update({
        "TESTING": True,
        "SECRET_KEY":"Ingenieriadesoftware10.$%&^_?",
    })

    # Inicialización de la base de datos
    
    yield app
    # apartir de aquí se pone el código para liberar los recursos 


@pytest.fixture(scope="session")
def client(app):
    #print("creando cliente...")
    return app.test_client()

def test_login(app, client):
    with client:
        response = client.get("/", follow_redirects=True)
        assert response.status_code == 200 