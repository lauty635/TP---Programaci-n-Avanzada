from pydantic import BaseModel
from typing import Optional

# Aca se estaria aplicando el modelado de datos
# Definimos como va a ser la estructura del TODO para que pueda recibir desde la
# API y que parametros vas a definir y de que tipo

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False