import pytest
import requests
from fueltrack.services.user.api_users import UserApi


HOST = "https://fueltrack-production-f193.up.railway.app"

@pytest.fixture(autouse=True,scope="session")
def init_environment():
    response = requests.get(url=f'{HOST}/health')
    assert response.status_code == 200

@pytest.fixture()
def create_user():
    api = UserApi()
    user = api.create_user()
    yield user
    api.delete_tg_id_user(user.tg_id,user.profile_name)
