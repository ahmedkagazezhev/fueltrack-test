import requests

from fueltrack.utils.helper import Helper
from fueltrack.services.user.payloads import Payload
from fueltrack.services.user.endpoints import Endpoint
from fueltrack.services.models.create_user_model import CreateUserResponse
from fueltrack.services.models.profile_summary import ProfileSummaryResponse
from fueltrack.services.models.user_profile_response import UserProfileResponse
from fueltrack.services.models.delete_user import DeleteUser


class UserApi(Helper):

    def __init__(self):
        super().__init__()
        self.payload = Payload()
        self.endpoint = Endpoint()

    def create_user(self):
        response = requests.post(url = self.endpoint.create_user,
                                 json=self.payload.create_user)
        assert response.status_code == 200 , response.json()
        model = CreateUserResponse(**response.json())
        return model.user

    def get_tg_id_user(self,tg_id):
        response = requests.get(url = self.endpoint.get_tg_id_user(tg_id))
        assert response.status_code == 200 , response.json()
        model = ProfileSummaryResponse(**response.json())
        return model.profiles

    def delete_tg_id_user(self):
        response = requests.delete(url = self.endpoint.delete_tg_id_user)
        assert response.status_code == 200 , response.json()
        model = DeleteUser(**response.json())
        return model

    def get_tg_id_profile_name_user(self):
        response = requests.get(url = self.endpoint.get_tg_id_profile_name_user)
        assert response.status_code == 200 , response.json()
        model = UserProfileResponse(**response.json())
        return model