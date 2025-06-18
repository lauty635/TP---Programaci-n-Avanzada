# schemas.py
from pydantic import BaseModel, ConfigDict

class Todo(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

    # Configuración para que Pydantic lea atributos ORM
    model_config = ConfigDict(from_attributes=True)
