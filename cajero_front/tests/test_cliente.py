import pytest
from src.app import create_app
from src.config import Config
from flask import jsonify
import json

@pytest.fixture(scope="session")
def app():
    # Setup de la apliacción 
    SECRET = Config()
    SECRET_KEY = SECRET.SECRET_KEY
    app = create_app()
    
    # Modo test para capturar las excepciones que lanza el servidor
    app.config.update({
        "TESTING": True,
        "SECRET_KEY":SECRET_KEY,
    })

    # Inicialización de la base de datos
    
    yield app
    # apartir de aquí se pone el código para liberar los recursos 


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()

def test_login(app, client):
    with client:
        response = client.get("/", follow_redirects=True)
        assert response.status_code == 200 

def test_validar_tarjeta_id_valido(app, client):
    with client:
        id_tarjeta = 1000
        response = client.post("/tarjeta", data={"num_tarjeta":id_tarjeta}, follow_redirects=True)
        assert response.status_code == 200 

def test_validar_tarjeta_id_invalido(app, client):
    with client:
        id_tarjeta = 9999
        response = client.post("/tarjeta", data={"num_tarjeta":id_tarjeta}, follow_redirects=True)
        assert response.status_code == 404 
        
def test_valida_formulario_Nip(app, client):
    response = client.get("/nip", follow_redirects=True)
    assert response.status_code == 200 

def test_validar_nip_id_invalido(app, client):
    with client.session_transaction() as session:
        session['num'] = 1021
    num_repeticiones = 3
    for _ in range(num_repeticiones):
        data = {
            'num_nip': 8115
        }
        response = client.post('/cuenta', data=data, follow_redirects=True)
        assert response.status_code == 404
        with client.session_transaction() as session:
            assert session.get('num') == 1021

def test_validar_nip_id_valido(app, client):
    with client.session_transaction() as session:
        session['num'] = 1021
    data = {
        'num_nip': 8112
    }
    response = client.post('/cuenta', data=data, follow_redirects=True)
    assert response.status_code == 200
    with client.session_transaction() as session:
        assert session.get('num') == 1021


def test_validar_retirar_valido(app, client):
    with client.session_transaction() as session:
        session['num'] = 1021
    data = {
        'pago': 50.0,
        'submit_retirar':'Retirar'
    }
    response = client.post('/retiro_deposito', data=data, follow_redirects=True)
    assert response.status_code == 200

    with client.session_transaction() as session:
        assert session.get('num') == 1021

def test_validar_retirar_invalido(app, client):
    with client.session_transaction() as session:
        session['num'] = 1021
    data = {
        'pago': 0.0,
        'submit_retirar':'Retirar'
    }
    response = client.post('/retiro_deposito', data=data, follow_redirects=True)
    assert response.status_code == 200

    with client.session_transaction() as session:
        assert session.get('num') == 1021


def test_validar_depositar_valido(app, client):
    with client.session_transaction() as session:
        session['num'] = 1021
    data = {
        'pago': 50.0,
        'submit_depositar':'Depositar'
    }
    response = client.post('/retiro_deposito', data=data, follow_redirects=True)
    assert response.status_code == 200

    with client.session_transaction() as session:
        assert session.get('num') == 1021







