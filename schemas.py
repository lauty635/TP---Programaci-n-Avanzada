# schemas.py
from pydantic import BaseModel, ConfigDict

# Para CREAR tareas (sin ID)
class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    
# Para RESPONDER (incluye ID generado por la BD)
class TodoResponse(TodoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
