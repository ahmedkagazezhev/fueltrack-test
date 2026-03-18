from pydantic import BaseModel,field_validator

class SaveFoodModel(BaseModel):
    success: bool
    id: int

    @field_validator("id")
    def field_id(cls,value):
        if value < 0:
            raise ValueError("id cannot be less than zero")
        return value
