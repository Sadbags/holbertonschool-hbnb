from flask import Blueprint, request, jsonify
from Model.user import User
from Persistence.DataManager import DataManager
import re

user_bp = Blueprint('user_bp', __name__)
data_manager = DataManager()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Ruta para crear un nuevo usuario
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_email(data.get('email')):
        return jsonify({'error': 'Invalid email format'}), 400
    if not data.get('first_name') or not data.get('last_name'):
        return jsonify({'error': 'First name and last name are required'}), 400
    if next((obj for obj in data_manager.storage.objects.values() if isinstance(obj, User) and obj.email == data['email']), None):
        return jsonify({'error': 'Email already exists'}), 409
    user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    data_manager.save(user)
    return jsonify({'id': str(user.id)}), 201

# Ruta para obtener la lista de todos los usuarios
@user_bp.route('/', methods=['GET'])
def get_users():
    users = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, User)]
    return jsonify(users)

# Ruta para obtener los detalles de un usuario específico por su ID
@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.__dict__)

# Ruta para actualizar la información de un usuario existente
@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    if 'email' in data and not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    if 'first_name' in data and not data['first_name']:
        return jsonify({'error': 'First name cannot be empty'}), 400
    if 'last_name' in data and not data['last_name']:
        return jsonify({'error': 'Last name cannot be empty'}), 400
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    data_manager.update(user)
    return jsonify({'id': str(user.id)}), 200

# Ruta para eliminar un usuario específico por su ID
@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    data_manager.delete(user_id, User)
    return '', 204
