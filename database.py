from sqlalchemy.exc import IntegrityError
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://localhost:6666/simon_decants?user=root&password=26deoctubrE26"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    # db.test = db.Table('test',
    #     db.Column('id', db.Integer, primary_key=True),
    #     db.Column('nombre', db.String(50), nullable=False),
    #     db.Column('apellido', db.String(50), nullable=False),
    #     db.Column('dni', db.Integer, unique=True, nullable=False),
    #     db.Column('fecha_nacimiento', db.Date, nullable=False),
    # )
    
    # if not os.path.exists('site.db'):
    #     with app.app_context():
    #         db.create_all()
    #         print('Base de datos creada')
    #         pass
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)        
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'fecha_nacimiento': self.fecha_nacimiento.isoformat()  # Formato ISO para la fecha
        }
def get_users():
    try:
        users = Test.query.all()
        return jsonify({'status': 200,'message': 'Users retrieved successfully','users': [users.serialize() for users in users]})
    except Exception as e:
            return jsonify({'status': 500,'message': 'Error retrieving users','error': str(e)})
        
def create_user(user_data):
    try:
        new_user = Test(id= "1",
                        nombre= user_data['nombre'],
                        apellido= user_data['apellido'],
                        dni= user_data['dni'],
                        fecha_nac="2001-10-26"
                        )  # Crear una nueva instancia del modelo Test con los datos del usuario
        db.session.add(new_user)  # Agregar el nuevo usuario a la sesión
        db.session.commit()  # Confirmar los cambios en la base de datos
        return jsonify({'status': 'success', 'message': 'User created successfully'}), 200
    except IntegrityError as e:
        db.session.rollback()  # Deshacer la sesión en caso de error
        return jsonify({'status': 'error', 'message': 'User already exists', 'error': str(e)}), 409
    except Exception as e:
        db.session.rollback()  # Deshacer la sesión en caso de error
        return jsonify({'status': 'error', 'message': 'Error creating user', 'error': str(e)}), 500
        












    # try:
    #     new_user = Test(**user)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return jsonify({'status': 'success', 'message': 'User created successfully'}), 200
    # except IntegrityError as e:
    #     db.session.rollback()
    #     return jsonify({'status': 'error', 'message': 'User already exists', 'error': str(e)}), 409
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({'status': 'error', 'message': 'Error creating user', 'error': str(e)}), 500

    # try:
    #     db.session.add(user)
    #     db.session.commit()
    #     return jsonify({'status': 'success', 'message': 'User created successfully'}), 200
    # except IntegrityError as e:
    #     db.session.rollback()
    #     return jsonify({'status': 'error', 'message': 'User already exists', 'error': str(e)}), 409
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({'status': 'error', 'message': 'Error creating user', 'error': str(e)}), 500