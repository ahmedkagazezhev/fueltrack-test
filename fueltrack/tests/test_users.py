import allure
import pytest
from fueltrack.config.base_test import BaseTest
from fueltrack.services.user.payloads import Payload
from fueltrack.services.food.payloads import PayloadsFood
from fueltrack.services.workout.payloads import PayloadWorkOut


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

    def test_delete_profile(self,create_user_for_delete):
        self.api_users.delete_tg_id_user(create_user_for_delete.tg_id,create_user_for_delete.profile_name)
        profile = self.api_users.get_tg_id_user(create_user_for_delete.tg_id)
        profiles_names = [p.profile_name for p in profile]
        assert create_user_for_delete.profile_name not in profiles_names

    @pytest.mark.parametrize("payloads",Payload().negative_payloads)
    def test_negative_create_user(self,payloads):
        response = self.api_users.create_user_raw(payloads)
        assert response.status_code == 400

    def test_analyze_food(self):
        result = self.api_food.analyze_food()
        assert result.dish is not None

    def test_analyze_food_image(self):
        result = self.api_food.analyze_food_image()
        assert result is not None

    def test_save_meal_db(self,create_user):
        self.api_food.save_food()
        assert self.api_food.save_food().success == True
        result = self.api_food.get_today_meals_and_tg(create_user.tg_id)
        print(result)
        dishes = [m.dish for m in result.meals]
        assert self.api_food.payload.save_food["dish"] in dishes

    def test_get_today_meals_and_tg(self,create_user):
        self.api_food.save_food()
        result = self.api_food.get_today_meals_and_tg(create_user.tg_id)
        print(result)
        dishes = [m.dish for m in result.meals]
        assert self.api_food.payload.save_food["dish"] in dishes

    def test_get_history_for_7_day(self,create_user):
        result = self.api_food.get_history_for_7_day(create_user.tg_id)
        assert result is not None

    @pytest.mark.parametrize("payloads", PayloadsFood().negative_analyze_food)
    def test_negative_analyze_food(self,payloads):
        response = self.api_food.analyze_food_raw(payloads)
        assert response.status_code == 400
        assert 'error' in response.json()

    def test_save_workout_set(self):
        result = self.api_workout.save_set()
        assert result.success == True

    def test_get_today_workouts(self,create_user):
        result = self.api_workout.get_today_workouts(create_user.tg_id)
        assert any(m.tg_id == create_user.tg_id for m in result)
        assert any(n.profile_name == create_user.profile_name for n in result)


    def test_get_distinct_exercises(self,create_user):
        self.api_workout.save_set()
        result = self.api_workout.get_exercises_user(create_user.tg_id)
        assert self.api_workout.payload.save_workout_set_payload["exercise"] in result

    def test_get_workout_history(self,create_user):
        self.api_workout.save_set()
        result = self.api_workout.get_workout_history(create_user.tg_id,self.api_workout.payload.save_workout_set_payload["exercise"])
        assert any(m.total_sets >= self.api_workout.payload.save_workout_set_payload["sets"] for m in result)
        assert any(m.total_reps >= self.api_workout.payload.save_workout_set_payload["reps"] for m in result)
        assert any(m.max_weight >= self.api_workout.payload.save_workout_set_payload["weight_kg"] for m in result)


    @pytest.mark.parametrize("payloads", PayloadWorkOut().negative_save_workout_payloads)
    def test_negative_save_workout_set(self,payloads):
        result = self.api_workout.negative_save_set(payloads)
        assert result.status_code == 400

    @pytest.mark.parametrize("payloads",PayloadWorkOut().negative_get_today_workouts)
    def test_negative_get_today_workouts(self,payloads):
        result = self.api_workout.negative_get_today_workouts(payloads)
        assert result.status_code == 400

    @pytest.mark.parametrize("payloads",PayloadWorkOut().negative_get_today_workouts)
    def test_negative_get_distinct_exercises(self,payloads):
        result = self.api_workout.negative_get_distinct_exercises(payloads)
        assert result.status_code == 400

    @pytest.mark.parametrize("payloads",PayloadWorkOut().negative_get_workout_history)
    def test_negative_get_workout_history(self,payloads):
        result = self.api_workout.negative_get_workout_history(payloads)
        assert result.status_code == 400