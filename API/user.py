from flask import Blueprint, request, jsonify
from user import User
from Persistence.DataManager import DataManager

user_bp = Blueprint('user_bp', __name__)
data_manager = DataManager()

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    data_manager.save(user)
    return jsonify({'id': str(user.id)}), 201

@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.__dict__)


@user_bp.route('/', methods=['GET'])
def get_users():
    users = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, User)]
    return jsonify(users)


@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    data_manager.update(user)
    return jsonify({'id': str(user.id)}), 200

@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    data_manager.delete(user_id, User)
    return '', 204
