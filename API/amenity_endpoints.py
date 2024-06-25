from flask import Blueprint, request, jsonify, abort, Blueprint
from Model.amenity import Amenity
from Persistence.DataManager import DataManager

amenity_bp = Blueprint('amenity', __name__)
data_manager = DataManager()

# Ruta para crear una nueva amenidad
@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400
    if next((obj for obj in data_manager.storage.objects.values() if isinstance(obj, Amenity) and obj.name == data['name']), None):
        return jsonify({'error': 'Amenity with this name already exists'}), 409
    amenity = Amenity(name=data['name'], Description=data.get('Description', ''), Type=data.get('Type', ''))
    data_manager.save(amenity)
    return jsonify({'id': str(amenity.id)}), 201

# Ruta para obtener la lista de todas las amenidades
@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    amenities = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Amenity)]
    return jsonify(amenities)

# Ruta para obtener los detalles de una amenidad específica por su ID
@amenity_bp.route('/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, Amenity)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.__dict__)

# Ruta para actualizar la información de una amenidad existente
@amenity_bp.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = data_manager.get(amenity_id, Amenity)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    if 'name' in data and not data['name']:
        return jsonify({'error': 'Name cannot be empty'}), 400
    if 'name' in data and next((obj for obj in data_manager.storage.objects.values() if isinstance(obj, Amenity) and obj.name == data['name']), None):
        return jsonify({'error': 'Amenity with this name already exists'}), 409
    for key, value in data.items():
        setattr(amenity, key, value)
    amenity.save()
    data_manager.update(amenity)
    return jsonify({'id': str(amenity.id)}), 200

# Ruta para eliminar una amenidad específica por su ID
@amenity_bp.route('/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, Amenity)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    data_manager.delete(amenity_id, Amenity)
    return '', 204
