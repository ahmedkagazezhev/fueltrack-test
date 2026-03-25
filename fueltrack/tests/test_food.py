import allure
import pytest
from fueltrack.config.base_test import BaseTest
from fueltrack.services.food.payloads import PayloadsFood

class TestFood(BaseTest):
    def test_analyze_food(self):
        result = self.api_food.analyze_food()
        assert result.dish is not None


    def test_analyze_food_image(self):
        result = self.api_food.analyze_food_image()
        assert result is not None


    def test_save_meal_db(self, create_user):
        self.api_food.save_food()
        assert self.api_food.save_food().success == True
        result = self.api_food.get_today_meals_and_tg(create_user.tg_id)
        dishes = [m.dish for m in result.meals]
        assert self.api_food.payload.save_food["dish"] in dishes


    def test_get_today_meals_and_tg(self, create_user):
        self.api_food.save_food()
        result = self.api_food.get_today_meals_and_tg(create_user.tg_id)
        dishes = [m.dish for m in result.meals]
        assert self.api_food.payload.save_food["dish"] in dishes


    def test_get_history_for_7_day(self, create_user):
        result = self.api_food.get_history_for_7_day(create_user.tg_id)
        assert result is not None


    # @pytest.mark.parametrize("payloads", PayloadsFood().negative_analyze_food)
    # def test_negative_analyze_food(self, payloads):
    #     response = self.api_food.analyze_food_raw(payloads)
    #     assert response.status_code == 400
    #     assert 'error' in response.json()