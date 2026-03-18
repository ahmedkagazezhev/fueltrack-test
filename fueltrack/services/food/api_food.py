import requests

from fueltrack.utils.helper import Helper
from fueltrack.services.food.payloads import PayloadsFood
from fueltrack.services.food.endpoints import EndpointFood
from fueltrack.services.models.food.analyze_food_model import AnalyzeFoodModel
from fueltrack.services.models.food.save_food_model import SaveFoodModel
from fueltrack.services.models.food.get_today_meals_and_tg_model import GetTodayMealsAndTgModel
from fueltrack.services.models.food.get_history_for_7_day_model import GetHistoryForSevenDay

class FoodApi(Helper):

    def __init__(self):
        super().__init__()
        self.endpoint = EndpointFood()
        self.payload = PayloadsFood()


    def analyze_food(self):
        response = requests.post(url=self.endpoint.analyze_food,json=self.payload.analyze_food)
        assert response.status_code == 200
        self.attach_response(response.json())
        model = AnalyzeFoodModel(**response.json())
        return model

    def analyze_food_image(self):
        response = requests.post(url=self.endpoint.analyze_food,json=self.payload.analyze_food_image)
        assert response.status_code == 200
        self.attach_response(response.json())
        model = AnalyzeFoodModel(**response.json())
        return model


    def save_food(self):
        response = requests.post(url = self.endpoint.save_food, json = self.payload.save_food)
        assert response.status_code == 200
        self.attach_response(response.json())
        model = SaveFoodModel(**response.json())
        return model

    def get_today_meals_and_tg(self,tg_id):
        response = requests.get(url = self.endpoint.get_today_meals_and_tg(tg_id))
        assert response.status_code == 200
        self.attach_response(response.json())
        model = GetTodayMealsAndTgModel(**response.json())
        return model

    def get_history_for_7_day(self,tg_id):
        response = requests.get(url = self.endpoint.get_history_for_7_day(tg_id))
        assert response.status_code == 200
        self.attach_response(response.json())
        model = GetHistoryForSevenDay(**response.json())
        return model.history

    def analyze_food_raw(self,payload):
        response = requests.post(url=self.endpoint.analyze_food,json=payload)
        self.attach_response(response.json())
        return response