import os
from dotenv import load_dotenv

load_dotenv()

class EndpointWorkOut:

    save_workout_set = f'{os.getenv("HOST")}/api/workout/save'

    get_today_workouts = lambda self, tgId : f'{os.getenv("HOST")}/api/workout/today/{tgId}'
    get_distinct_exercises = lambda self, tgId : f'{os.getenv("HOST")}/api/workout/exercises/{tgId}'
    get_workout_history = lambda self, tgId, exercise : f'{os.getenv("HOST")}/api/workout/history/{tgId}/{exercise}'