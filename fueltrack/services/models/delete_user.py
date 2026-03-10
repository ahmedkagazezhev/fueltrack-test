from pydantic import BaseModel, field_validator

class DeleteUser(BaseModel):
    success : bool
