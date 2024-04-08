from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://localhost:6666/simon_decants?user=root&password=26deoctubrE26"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    db.test = db.Table('test',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('nombre', db.String(50), nullable=False),
        db.Column('apellido', db.String(50), nullable=False),
        db.Column('dni', db.Integer, unique=True, nullable=False),
        db.Column('fecha_nacimiento', db.Date, nullable=False),
    )
    
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
            print('Base de datos creada')
            pass