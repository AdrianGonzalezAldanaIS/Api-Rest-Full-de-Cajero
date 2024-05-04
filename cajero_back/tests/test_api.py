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