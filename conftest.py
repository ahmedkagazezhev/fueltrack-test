import pytest
import requests


HOST = "https://fueltrack-production-f193.up.railway.app"

@pytest.fixture(autouse=True,scope="session")
def init_environment():
    response = requests.get(url=f'{HOST}/health')
    assert response.status_code == 200