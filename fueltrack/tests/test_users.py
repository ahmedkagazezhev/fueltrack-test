import allure
import pytest
from fueltrack.config.base_test import BaseTest

@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self,create_user):
        assert create_user.model_dump() == self.api_users.get_tg_id_profile_name_user(create_user.tg_id, create_user.profile_name).model_dump()

    def test_get_profiles(self,create_user):
        profile = self.api_users.get_tg_id_user(create_user.tg_id)
        profiles_names = [p.profile_name for p in profile]
        assert create_user.profile_name in profiles_names