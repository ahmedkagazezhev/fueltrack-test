from pydantic import BaseModel,field_validator
from datetime import datetime


class Total(BaseModel):
    calories: float
    protein: float
    fat: float
    carbs: float

    @field_validator("calories","protein","fat","carbs")
    def field_calories(cls,value):
        if value < 0 :
            raise ValueError("Cannot be less than zero")
        return value

class Meals(BaseModel):
    id: int
    tg_id: int
    profile_name: str
    dish: str
    calories: float
    protein: float
    fat: float
    carbs: float
    created_at: str

    @field_validator("calories","protein","fat","carbs","id")
    def field_calories_meals(cls,value):
        if value < 0 :
            raise ValueError("Cannot be less than zero")
        return value

    @field_validator("tg_id")
    def field_tg_id(cls,value):
        if value <= 0 :
            raise ValueError("Cannot be less than zero")
        return value

    @field_validator("profile_name","dish")
    def field_profile_name(cls,value):
        if value == "" or value is None :
            raise ValueError("Empty")
        return value

    @field_validator("created_at")
    def valid_datetime(cls, value):
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("Must be valid ISO datetime")
        return value

class GetTodayMealsAndTgModel(BaseModel):
    meals: list[Meals]
    totals: Total