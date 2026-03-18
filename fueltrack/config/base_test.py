from fueltrack.services.user.api_users import UserApi
from fueltrack.services.food.api_food import FoodApi
from fueltrack.services.workout.api_workout import WorkOutApi

class BaseTest:

    def setup_method(self):
        self.api_users = UserApi()
        self.api_food = FoodApi()
        self.api_workout = WorkOutApi()
