from pydantic import BaseModel,field_validator

class AnalyzeFoodModel(BaseModel):
    dish: str
    calories: float
    protein: float
    fat: float
    carbs: float

    @field_validator("dish")
    def field_dish(cls,value):
        if value == "" or value is None:
            raise ValueError("Dish not be empty")
        return value

    @field_validator("calories","protein","fat","carbs")
    def field_calories(cls,value):
        if value <0:
            raise ValueError("Cannot be less than zero")
        return value


