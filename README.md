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

## Diagrama del proyecto

![Diagrama General](https://raw.githubusercontent.com/lauty635/TP---Programaci-n-Avanzada/refs/heads/main/Diagrama_general.png)

## Diagrama de base de datos
![Diagrama Base de Datos](https://raw.githubusercontent.com/lauty635/TP---Programaci-n-Avanzada/refs/heads/main/Diagrama_bases_de_datos.png)

## Arquitectura MVC:
![MVC](https://raw.githubusercontent.com/lauty635/TP---Programaci-n-Avanzada/refs/heads/main/Arquitectura%20MVC.png)


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
## Presentación
(https://docs.google.com/presentation/d/1XuuBfI7obzVgN_FMjbY-V9Zz9DI52KtCI_o-0waiHr0/edit?slide=id.g3625cff3bb5_0_163#slide=id.g3625cff3bb5_0_163)

## Informe
(https://docs.google.com/document/d/1A4yrSpmds7TlZYCrkhjc7PQJjc5RLW8HgQx4XA4q8uA/edit?usp=sharing)
