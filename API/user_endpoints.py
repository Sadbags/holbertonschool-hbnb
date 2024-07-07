from flask import Blueprint, request, jsonify, abort
from Model.user import User
from Persistence.DataManager import DataManager
from database import db


user_blueprint = Blueprint('user_blueprint', __name__)
data_manager = DataManager()


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        abort(400, description="Missing required fields")

    email = request.json['email']
    if '@' not in email:
        abort(400, description="Invalid email format")

    if User.query.filter_by(email=email).first():
        abort(409, description="Email already exists")

    user = User(
        email=email,
        password=request.json['password'],
        is_admin=request.json.get('is_admin', False),
        password_hash=request.json.get('password_hash', ''),
        first_name=request.json.get('first_name', ''),
        last_name=request.json.get('last_name', '')
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict()), 200


@user_blueprint.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")

    if not request.json:
        abort(400, description="Missing required fields")

    user.email = request.json.get('email', user.email)
    user.first_name = request.json.get('first_name', user.first_name)
    user.last_name = request.json.get('last_name', user.last_name)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    db.session.delete(user)
    db.session.commit()
    return '', 204
