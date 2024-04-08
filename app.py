from flask import Flask, request
from .database import init_db

def create_app():
    app = Flask(__name__)
    
    init_db(app)


    # from . import usuario_bp

    # app.register_blueprint(usuario_bp.usuario_bp)

    
    @app.route('/')
    def home():
        # users = Users.query.all()
        # print(users)
        return 'Hello!'

    return app
    
    

