# TP - Programación Avanzada

Este repositorio contiene el desarrollo del trabajo práctico realizado por los estudiantes para la materia **Programación Avanzada**.

---

## Configuración del entorno

### 1. Crear un entorno virtual

```bash
python3 -m venv venv
```

### 2. Activar el entorno virtual

```bash
source venv/bin/activate
```

- Si estás en **Windows**, la activación del entorno virtual es:

```bash
.\venv\Scripts\activate
```

> **¿Para qué sirve esto?**  
Nos permite mantener el proyecto en onda, para que todos podamos correr el mismo codigo, sin diferencias de las versiones ya que eso nos puede generar conflictos en las depedencias xD
---

## Instalacion de dependencias

Una vez activado el entorno virtual, ejecutá:

```bash
pip install -r requirements.txt
```

> Sirve para instalar las dependencias que vamos a usar.

---

## Cómo ejecutar la aplicación

Para correr este programa es:


```bash
uvicorn main:app --reload
```

---

## Formas de comunicarnos con FastAPI

1. A través de la web, usando la interfaz gráfica.

Agregar video como seria.

---

2. A través de la consola o mediante peticiones POST a través de la API.

## Ejemplos de comunicación con FastAPI usando `curl`

1. **Obtener todos los "todos" (GET /todos)**

```bash
curl -X GET http://127.0.0.1:8000/todos
```

2. **Crear un nuevo "todo" (POST /todos)**

```bash
curl -X POST http://127.0.0.1:8000/todos \
    -H "Content-Type: application/json" \
    -d '{"id":1,"title":"Aprender FastAPI","completed":false}'
```

3. **Actualizar un "todo" existente (PUT /todos/{todo_id})**

```bash
curl -X PUT http://127.0.0.1:8000/todos/1 \
    -H "Content-Type: application/json" \
    -d '{"id":1,"title":"Aprender FastAPI avanzado","completed":true}'
```

4. **Eliminar un "todo" (DELETE /todos/{todo_id})**

```bash
curl -X DELETE http://127.0.0.1:8000/todos/1
```

5. **Consultar información de la API (GET /api)**

```bash
curl -X GET http://127.0.0.1:8000/api
```


# Usando Postman

Aca iria el video

y con la descripcion tecnica


subir como funcionancia los comandos de sql

Estructura del proyecto.

```
├── database.py
├── main.py
├── models.py
├── README.md
├── requirements.txt
├── schemas.py
├── static
│   ├── favicon.ico
│   └── index.html
├── todo_api_uml
├── todo_classes.py
├── todos.db
```
