from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # tu Base declarative


# Aca se estaria aplicando el modelado de datos
# Definimos como va a ser la estructura del TODO para que pueda recibir desde la
# API y que parametros vas a definir y de que tipo
class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)  # <-- ¡sin coma al final!

