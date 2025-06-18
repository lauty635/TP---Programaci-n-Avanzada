from abc import ABC, abstractmethod
# Si necesitas importar el modelo Pydantic o SQLAlchemy, hazlo aquí
# from models import Todo as TodoPydantic
# from models_db import TodoDB

class TaskBase(ABC):
    """
    Clase base abstracta para una tarea.
    Define la estructura que toda tarea debe tener.
    """

    def __init__(self, title: str, description: str = "", completed: bool = False):
        # Propiedades privadas protegidas con encapsulación
        self._title = title
        self._description = description
        self._completed = completed

    @property
    def title(self):
        # Getter para el título
        return self._title

    @title.setter
    def title(self, value):
        # Setter para el título con validación
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def description(self):
        # Getter para la descripción
        return self._description

    @description.setter
    def description(self, value):
        # Setter para la descripción
        self._description = value

    @property
    def completed(self):
        # Getter para el estado completado
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        # Setter para el estado completado
        self._completed = value

    @abstractmethod
    def toggle_completed(self):
        # Método abstracto que debe implementar la subclase
        pass

    def __str__(self):
        # Método para representar la tarea como texto
        return f"Task: {self.title} | Completed: {self.completed}"


class Todo(TaskBase):
    """
    Implementación concreta de la tarea.
    """

    def toggle_completed(self):
        # Cambia el estado completado al contrario
        self.completed = not self.completed

    def to_dict(self):
        # Convertir objeto a diccionario para serialización
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
