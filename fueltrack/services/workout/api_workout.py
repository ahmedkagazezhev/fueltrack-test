import requests

from fueltrack.utils.helper import Helper
from fueltrack.services.workout.payloads import PayloadWorkOut
from fueltrack.services.workout.endpoints import EndpointWorkOut
from fueltrack.services.models.workout.save_set_model import SaveSetModel
from fueltrack.services.models.workout.get_today_workout_model import GetTodayWorkoutModel
from fueltrack.services.models.workout.get_exercises_user_model import GetExercisesUserModel
from fueltrack.services.models.workout.get_workout_history_model import GetWorkoutHistoryModel

class WorkOutApi(Helper):

    def __init__(self):
        super().__init__()
        self.endpoint = EndpointWorkOut()
        self.payload = PayloadWorkOut()


    def save_set(self):
        response = requests.post(url=self.endpoint.save_workout_set, json= self.payload.save_workout_set_payload)
        assert response.status_code == 200
        self.attach_response(response.json())
        model = SaveSetModel(**response.json())
        return model

    def get_today_workouts(self,tg_id):
        response = requests.get(url= self.endpoint.get_today_workouts(tg_id))
        assert response.status_code == 200
        self.attach_response(response.json())
        model = GetTodayWorkoutModel(**response.json())
        return model.workouts

    def get_exercises_user(self,tg_id):
        response = requests.get(url= self.endpoint.get_distinct_exercises(tg_id))
        assert response.status_code == 200
        self.attach_response(response.json())
        model = GetExercisesUserModel(**response.json())
        return model.exercises

    def get_workout_history(self,tg_id,exercise):
        response = requests.get(url= self.endpoint.get_workout_history(tg_id,exercise))
        assert response.status_code == 200
        self.attach_response(response.json())
        model = GetWorkoutHistoryModel(**response.json())
        return model.history

    def negative_save_set(self,payload):
        response = requests.post(url=self.endpoint.save_workout_set, json= payload)
        self.attach_response(response.json())
        return response

    def negative_get_today_workouts(self,payload):
        response = requests.get(url=self.endpoint.get_today_workouts(payload))
        self.attach_response(response.json())
        return response

    def negative_get_distinct_exercises(self,payload):
        response = requests.get(url=self.endpoint.get_distinct_exercises(payload))
        self.attach_response(response.json())
        return response

    def negative_get_workout_history(self,payload):
        response = requests.get(url=self.endpoint.get_workout_history(payload["tg_id"],payload["exercise"]))
        self.attach_response(response.json())
        return response