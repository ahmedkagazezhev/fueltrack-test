from pydantic import BaseModel, field_validator
from datetime import datetime

class UserProfile(BaseModel):
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

    @field_validator("profile_name", "name", "gender", "goal", "activity")
    def string_not_empty(cls, value):
        if value is None or value.strip() == "":
            raise ValueError("Field cannot be empty")
        return value

    @field_validator("tg_id", "age", "height", "weight", "daily_calories")
    def must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Must be positive")
        return value



class CreateUserResponse(BaseModel):
    success: bool
    user: UserProfile