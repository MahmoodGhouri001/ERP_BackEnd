from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from .config import databaseconfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseconfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ae9e9de7906d0f1fd417c1ea75c02c70'

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Configuration and extensions setup

# Register blueprints
from app.auth.routes import auth_bp
from app.branch.routes import branches_bp

app.register_blueprint(auth_bp)
app.register_blueprint(branches_bp)
