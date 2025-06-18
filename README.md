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


