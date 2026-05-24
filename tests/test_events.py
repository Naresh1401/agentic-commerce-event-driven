from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app, raise_server_exceptions=False)

def test_event_log_after_product_search():
    client.get('/products', params={'query': 'pasta'})
    response = client.get('/events')
    assert response.status_code == 200
    assert any(event['event_type'] == 'product_viewed' for event in response.json()['items'])

