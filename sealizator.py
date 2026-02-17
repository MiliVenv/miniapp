from pydantic import BaseModel, ConfigDict

class TaskSchema(BaseModel):
    id: int
    title: str
    completed: bool
    user: int

    model_config = ConfigDict(from_attributes=True)