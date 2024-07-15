import pytest
from flask import json
from api.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_evaluate_ethics(client):
    """Test the ethics evaluation endpoint."""
    response = client.post('/api/evaluate/ethics', json={"data": "test data"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'ethical'

def test_evaluate_sustainability(client):
    """Test the sustainability evaluation endpoint."""
    response = client.post('/api/evaluate/sustainability', json={"data": "test data"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'sustainable'
