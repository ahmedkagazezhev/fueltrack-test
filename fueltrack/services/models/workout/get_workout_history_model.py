from pydantic import BaseModel,field_validator
from datetime import date

class History(BaseModel):
    date: date
    max_weight: int
    total_sets: int
    total_reps: int

    @field_validator("max_weight","total_sets","total_reps")
    def field_max_weight_total_sets_reps(cls,value):
        if value <=0:
            raise ValueError("Field cannot be empty")
        return value

class GetWorkoutHistoryModel(BaseModel):
    history: list[History]