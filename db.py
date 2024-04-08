from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import os



# util para depurar echo=True

class Users:
    def __init__(self, id, name, last_name, email, normal_email, password, phone, type):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.normal_email = normal_email
        self.password = password
        self.phone = phone
        self.type = type


db_url = "jdbc:mysql://localhost:6666/simon_decants?user=root&password=26deoctubrE26"
engine = create_engine(db_url)
# Crear una conexión a la base de datos
# Definir la tabla 
metadata = MetaData()
users = Table('users', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('last_name', String),
                 Column('email', String),
                 Column('normal_email', String),
                 Column('password', String),
                 Column('phone', Integer),
                 Column('type', String),
                 )
    
# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar la tabla y guardar cada fila como un objeto Users en un array
filas = session.query(users).all()
objetos = [Users(id=row.id, name=row.name, last_name=row.last_name, email=row.email, normal_email=row.normal_email, password=row.password, phone=row.phone, type=row.type) for row in filas]

# Ahora 'objetos' contiene cada fila como un objeto Users
for obj in objetos:
    print(f"ID: {obj.id}, Nombre: {obj.name}, Apellido: {obj.last_name}, Email: {obj.email}, Email Normal: {obj.normal_email}, Contraseña: {obj.password}, Teléfono: {obj.phone}, Tipo: {obj.type}")

# No olvides cerrar la sesión cuando hayas terminado
session.close()