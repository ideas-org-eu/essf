import pytest
from flask import json
from essf.api.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_evaluate_ethics(client):
    response = client.post('/api/evaluate/ethics', json={
        "fair_wages": True,
        "safe_conditions": True,
        "child_labor": False,
        "transparency": True,
        "corruption": False,
        "data_protection_compliance": True,
        "privacy_protection": True
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] in ['Ethical', 'Needs Improvement']

def test_evaluate_sustainability(client):
    response = client.post('/api/evaluate/sustainability', json={
        "emissions": 50,
        "industry_average_emissions": 100,
        "recycling_program": True,
        "waste_reduction": True,
        "water_efficiency": True,
        "energy_efficiency": True,
        "uses_renewable_energy": True
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] in ['Sustainable', 'Needs Improvement']
