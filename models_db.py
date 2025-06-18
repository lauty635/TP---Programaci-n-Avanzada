from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True) # Clave primaria y indice
    title = Column(String, nullable=False) # Titulo obligatorio
    description = Column(String) # Descripcion opcional
    completed = Column(Boolean, default=False) # Estado por defecto (No hecho)


