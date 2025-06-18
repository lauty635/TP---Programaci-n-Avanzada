from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import List
from models import Todo
import os
from database import Base, engine
from models import TodoDB

# Creamos la tabla en la base al iniciar la app
Base.metadata.create_all(bind=engine)



app = FastAPI(title="To-Do API", description="API para gestionar tareas")

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear directorio static si no existe
if not os.path.exists("static"):
    os.makedirs("static")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Base de datos simulada (en memoria)
todos: List[Todo] = []

# Redireccionar la raíz a la interfaz web
@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")

@app.get("/api")
def api_info():
    return {"message": "To-Do API con FastAPI", "docs": "/docs", "app": "/static/index.html"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="ID ya existe")
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            # Mantener el mismo ID
            updated_todo.id = todo_id
            todos[idx] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[idx]
            return {"message": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")  