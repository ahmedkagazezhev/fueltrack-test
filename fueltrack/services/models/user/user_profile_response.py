from pydantic import BaseModel, field_validator
from datetime import datetime

class UserProfileResponse(BaseModel):
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

    @field_validator("profile_name","name", "goal", "activity")
    def fields_profile_name_name_goal(cls,value):
        if value == "" or value is None:
            raise ValueError("Field cannot be empty")
        else:
            return value

    @field_validator("gender")
    def gender_is_valid(cls, value):
        if value not in ["male", "female"]:
            raise ValueError("Gender must be 'male' or 'female'")
        return value

    @field_validator("tg_id")
    def fields_tg_id(cls,value):
        if value <= 0:
            raise ValueError("tg_id must be positive")
        else:
            return value

    @field_validator("age")
    def age_is_valid(cls, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        if value > 120:
            raise ValueError("Age is unrealistic")
        return value

    @field_validator("height")
    def height_is_valid(cls, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        if value > 250:
            raise ValueError("Height is unrealistic")
        return value

    @field_validator("weight")
    def weight_is_valid(cls, value):
        if value <= 0:
            raise ValueError("Weight must be positive")
        if value > 300:
            raise ValueError("Weight is unrealistic")
        return value

    @field_validator("daily_calories")
    def calories_are_positive(cls, value):
        if value <= 0:
            raise ValueError("daily_calories must be positive")
        return value

    @field_validator("created_at")
    def created_at_is_valid(cls, value):
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("created_at must be valid ISO datetime")
        return value

