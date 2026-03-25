import allure
import pytest
from fueltrack.config.base_test import BaseTest
from fueltrack.services.workout.payloads import PayloadWorkOut

@pytest.mark.workout
class TestWorkOut(BaseTest):
    def test_save_workout_set(self):
        result = self.api_workout.save_set()
        assert result.success == True

    def test_get_today_workouts(self, create_user):
        result = self.api_workout.get_today_workouts(create_user.tg_id)
        assert any(m.tg_id == create_user.tg_id for m in result)
        assert any(n.profile_name == create_user.profile_name for n in result)

    def test_get_distinct_exercises(self, create_user):
        self.api_workout.save_set()
        result = self.api_workout.get_exercises_user(create_user.tg_id)
        assert self.api_workout.payload.save_workout_set_payload["exercise"] in result

    def test_get_workout_history(self, create_user):
        self.api_workout.save_set()
        result = self.api_workout.get_workout_history(create_user.tg_id,
                                                      self.api_workout.payload.save_workout_set_payload["exercise"])
        assert any(m.total_sets >= self.api_workout.payload.save_workout_set_payload["sets"] for m in result)
        assert any(m.total_reps >= self.api_workout.payload.save_workout_set_payload["reps"] for m in result)
        assert any(m.max_weight >= self.api_workout.payload.save_workout_set_payload["weight_kg"] for m in result)

    # @pytest.mark.parametrize("payloads", PayloadWorkOut().negative_save_workout_payloads)
    # def test_negative_save_workout_set(self, payloads):
    #     result = self.api_workout.negative_save_set(payloads)
    #     assert result.status_code == 400
    #
    # @pytest.mark.parametrize("payloads", PayloadWorkOut().negative_get_today_workouts)
    # def test_negative_get_today_workouts(self, payloads):
    #     result = self.api_workout.negative_get_today_workouts(payloads)
    #     assert result.status_code == 400
    #
    # @pytest.mark.parametrize("payloads", PayloadWorkOut().negative_get_today_workouts)
    # def test_negative_get_distinct_exercises(self, payloads):
    #     result = self.api_workout.negative_get_distinct_exercises(payloads)
    #     assert result.status_code == 400
    #
    # @pytest.mark.parametrize("payloads", PayloadWorkOut().negative_get_workout_history)
    # def test_negative_get_workout_history(self, payloads):
    #     result = self.api_workout.negative_get_workout_history(payloads)
    #     assert result.status_code == 400