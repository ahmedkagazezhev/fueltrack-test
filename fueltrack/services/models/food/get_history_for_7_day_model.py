from pydantic import BaseModel,field_validator
from datetime import datetime,date

class History(BaseModel):
    date: date
    calories: float
    protein: float
    fat: float
    carbs: float

    @field_validator("calories","protein","fat","carbs")
    def field_calories_history(cls,value):
        if value < 0 :
            raise ValueError("Cannot be less than zero")
        return value



class GetHistoryForSevenDay(BaseModel):
    history: list[History]