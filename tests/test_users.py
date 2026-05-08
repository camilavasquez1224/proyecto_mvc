import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_health(client):
    response = client.get('/users/health')
    assert response.status_code == 200

def test_crear_usuario(client):
    response = client.post('/users/', json={
        'name': 'Test User',
        'email': 'test@email.com'
    })
    assert response.status_code == 201

def test_obtener_usuarios(client):
    response = client.get('/users/')
    assert response.status_code == 200

def test_actualizar_usuario(client):
    client.post('/users/', json={'name': 'Juan', 'email': 'juan@email.com'})
    response = client.put('/users/1', json={'name': 'Juan Actualizado', 'email': 'juan@email.com'})
    assert response.status_code == 200

def test_eliminar_usuario(client):
    client.post('/users/', json={'name': 'Juan', 'email': 'juan@email.com'})
    response = client.delete('/users/1')
    assert response.status_code == 200