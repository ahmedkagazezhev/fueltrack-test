from pydantic import BaseModel

class GetExercisesUserModel(BaseModel):
    exercises: list[str]

