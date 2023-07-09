from flask import Blueprint, request, jsonify
from .models import db, Users
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from app.schemas.user import user_schema, users_schema

auth_bp = Blueprint('auth', __name__)

# Define routes for authentication
@auth_bp.route('/api/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']

    existing_user = Users.query.filter_by(username=username).first()

    if existing_user:
        return jsonify(message=f'Username already exists: {username}'), 409

    new_user = Users(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User created successfully',new_user=user_schema.dump(new_user)), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    users = Users.query.filter_by(username=username).first()

    if users and users.check_password(password):
        access_token = create_access_token(identity=users.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401
