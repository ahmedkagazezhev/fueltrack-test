from pydantic import BaseModel, field_validator
from datetime import datetime

class GetFirstProfileUserMode(BaseModel):
    tg_id: int
    profile_name: str
    name: str
    gender: str
    age: int
    height: int
    weight: int
    goal: str
    activity: str
    daily_calories: int
    created_at: datetime

    @field_validator("tg_id","age","height","weight")
    def field_first_int(cls,value):
        if value <= 0:
            raise ValueError("not be less then zero")
        return value

    @field_validator("daily_calories")
    def field_daily_calories_int(cls,value):
        if value < 0:
            raise ValueError("not be less then zero")
        return value

    @field_validator("profile_name","name","gender","goal","activity")
    def field_first_int(cls,value):
        if value == "" or value is None:
            raise ValueError("Field not be empty")
        return value