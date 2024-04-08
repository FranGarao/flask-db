from flask import Flask, jsonify, request
from .database import init_db, get_users, create_user, Test, db
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    
    init_db(app)

    CORS(app)
    # from . import usuario_bp

    # app.register_blueprint(usuario_bp.usuario_bp)

    
    @app.route('/')
    def index():
        # users = Users.query.all()
        # print(users)
        return 'Hello!'  
    @app.route('/home')
    def home():
        
        try: 
            response = get_users()
            return response
        except Exception as e:
            return jsonify({'status': 500,'message': 'Error retrieving users','error': str(e)})

    @app.route('/sasas', methods=['POST'])
    def create_userr():
        if request.method == 'POST':
            user = request.get_json()
            usern= [user for user in user]
            print("".join(usern))
            
            create_user(user)
            if create_user(user):
                return jsonify({"message": "User created successfullyyyyyyxd", "user": user}), 201
        else:
        # Si la solicitud no es un POST, devuelve un error 405 (Method Not Allowed)
            return jsonify({"error": "Method not allowed"}), 405

        
    @app.route('/create', methods=['POST'])
    def crr():
        user = request.json
        data = {"name": user['name'], "last_name": user['apellido'], "dni": user['dni'], "fecha_nacimiento": user['fecha_nacimiento']}
        print(data.get('name'))
        new_user = Test(id= 888,
                        nombre= data.get('name'),
                        apellido= data.get('last_name'),
                        dni= data.get('dni'),
                        fecha_nacimiento=data.get('fecha_nacimiento')
                        )    # Crear una nueva instancia del modelo Test con los datos del usuario
        db.session.add(new_user)  # Agregar el nuevo usuario a la sesión
        db.session.commit()  # Confirmar los cambios en la base de datos
        return jsonify({'status': 'success', 'message': 'User created successfully'}), 200
    return app
    
    

