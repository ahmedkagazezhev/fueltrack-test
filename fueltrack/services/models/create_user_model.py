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
    created_at: str

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

    @field_validator("created_at")
    def valid_datetime(cls, value):
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("Must be valid ISO datetime")
        return value

class CreateUserResponse(BaseModel):
    success: bool
    user: UserProfile