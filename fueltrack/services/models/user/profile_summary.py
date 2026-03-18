from pydantic import BaseModel, field_validator

class ProfileSummary(BaseModel):
    profile_name: str
    goal: str
    daily_calories: int
    name: str

    @field_validator("profile_name","goal","name")
    def fields_profile_name_name_goal(cls,value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

    @field_validator("daily_calories")
    def fields_daily_calories(cls,value):
        if value <= 0:
            raise ValueError("Daily calories must be positive")
        else:
            return value



class ProfileSummaryResponse(BaseModel):
    profiles: list[ProfileSummary]

    @field_validator("profiles")
    def fields_profiles(cls,value):
        if len(value) == 0:
            raise ValueError("Profiles list cannot be empty")
        return value