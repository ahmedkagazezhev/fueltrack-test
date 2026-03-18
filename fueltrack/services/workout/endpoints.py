HOST = "https://fueltrack-production-f193.up.railway.app"

class EndpointWorkOut:

    save_workout_set = f'{HOST}/api/workout/save'

    get_today_workouts = lambda self, tgId : f'{HOST}/api/workout/today/{tgId}'
    get_distinct_exercises = lambda self, tgId : f'{HOST}/api/workout/exercises/{tgId}'
    get_workout_history = lambda self, tgId, exercise : f'{HOST}/api/workout/history/{tgId}/{exercise}'