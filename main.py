from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import List
import os
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Todo, TodoDB

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


# Redireccionar la raíz a la interfaz web
@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")

@app.get("/api")
def api_info():
    return {"message": "To-Do API con FastAPI", "docs": "/docs", "app": "/static/index.html"}

# Obtener todos los todos de la base de datos
@app.get("/todos", response_model=List[Todo])
def get_todos(db: Session = Depends(get_db)):
    todos_db = db.query(TodoDB).all()
    return todos_db

# Obtenemos los ID de los TODO
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int, db : Session = Depends(get_db)):
        todo_db = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
        if not todo_db:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return todo_db

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo, db: Session = Depends(get_db)):    
    # Verificamos que el ID exista
    existing = db.query(TodoDB).filter(TodoDB.id == todo.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="ID ya existe")
    todo_db = TodoDB(**todo.dict())
    db.add(todo_db)
    db.commit()
    db.refresh(todo_db)
    return todo_db

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
    todo_db = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if not todo_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    for key, value in updated_todo.dict().items():
        setattr(todo_db, key, value)

    db.commit()
    db.refresh(todo_db)
    return todo_db

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_db = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if not todo_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(todo_db)
    db.commit()
    return {"message": "Tarea eliminada"}

