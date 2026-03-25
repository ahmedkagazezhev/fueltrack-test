import allure
import pytest
from fueltrack.config.base_test import BaseTest
from fueltrack.services.user.payloads import Payload
from fueltrack.services.food.payloads import PayloadsFood
from fueltrack.services.workout.payloads import PayloadWorkOut


@allure.epic("Administration")
@allure.feature("Users")
@pytest.mark.users
class TestUsers(BaseTest):

    @allure.title("Create new user")
    def test_create_user(self,create_user):
        assert create_user.model_dump() == self.api_users.get_tg_id_profile_name_user(create_user.tg_id, create_user.profile_name).model_dump()

    def test_get_first_profile_user(self,create_user):
        result = self.api_users.get_first_profile_user(create_user.tg_id)
        assert create_user.tg_id == result.tg_id
        assert result.profile_name is not None

    def test_get_profiles(self,create_user):
        profile = self.api_users.get_tg_id_user(create_user.tg_id)
        profiles_names = [p.profile_name for p in profile]
        assert create_user.profile_name in profiles_names

    def test_delete_profile(self,create_user_for_delete):
        self.api_users.delete_tg_id_user(create_user_for_delete.tg_id,create_user_for_delete.profile_name)
        profile = self.api_users.get_tg_id_user(create_user_for_delete.tg_id)
        profiles_names = [p.profile_name for p in profile]
        assert create_user_for_delete.profile_name not in profiles_names

    # @pytest.mark.parametrize("payloads",Payload().negative_payloads)
    # def test_negative_create_user(self,payloads):
    #     response = self.api_users.create_user_raw(payloads)
    #     assert response.status_code == 400

