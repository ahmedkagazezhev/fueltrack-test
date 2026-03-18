from pydantic import BaseModel, field_validator
from datetime import datetime

class Workout(BaseModel):
    id: int
    tg_id: int
    profile_name: str
    exercise: str
    weight_kg: int
    sets: int
    reps: int
    created_at: datetime

    @field_validator("weight_kg","sets","reps")
    def field_weight_sets_reps_one(cls,value):
        if value <= 0:
            raise ValueError("Not be less then zero")
        return value

    @field_validator("id","tg_id")
    def field_tg_id_id(cls,value):
        if value < 0:
            raise ValueError("Not be less then zero")
        return value

    @field_validator("profile_name","exercise")
    def field_profile_name_exercise_one(cls,value):
        if value == "" or value is None:
            raise ValueError("Field cannot be empty")
        return value

class GetTodayWorkoutModel(BaseModel):
    workouts: list[Workout]