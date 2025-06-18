from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos el URL
DATABASE_URL = "sqlite:///./todos.db"

# Lo que hace es basicamentamente se arrancar el comunicador entre sqlite y python
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

# Creamos el contructor que le pedimos que debemos hacer un commit para confirmar lo cambios y tambien decimos que los cambios no se envian automaticamente a la base de datos antes de cada consulta
# Por ultimo definimos cual se ver la session que nos conecte a la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Creamos la clase base que nos sirve para definir el modelado de datos.
Base = declarative_base()

# Sirve pa' agarrar la conexión a la base de datos, que después la usás tranqui en cualquier parte
def get_db():
    db = SessionLocal()  # Abrimos la puerta pa' la base
    try:
        yield db  # Te tiro la sesión activa, usala bien
    finally:
        db.close()  # Cierro la puerta pa' que no quede nada abierto y no jodamos
