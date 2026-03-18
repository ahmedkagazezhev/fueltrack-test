from pydantic import BaseModel,field_validator

class SaveSetModel(BaseModel):
    success: bool
    id: int

    @field_validator("id")
    def field_id(cls,value):
        if value < 0:
            raise ValueError("Field not be empty")
        return value
