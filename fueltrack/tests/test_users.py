import allure
import pytest
from fueltrack.config.base_test import BaseTest


class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        print(user)
        print(self.api_users.get_tg_id_user(user.tg_id))