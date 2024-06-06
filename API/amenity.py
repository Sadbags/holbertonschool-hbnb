from flask import Blueprint, request, jsonify
from amenity import Amenity
from Persistence.DataManager import DataManager

amenity_bp = Blueprint('amenity', __name__)
data_manager = DataManager()

@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data['name'], description=data['description'], type=data['type'])
    data_manager.save(amenity)
    return jsonify({'id': str(amenity.id)}), 201

@amenity_bp.route('/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, Amenity)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.__dict__)

@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    amenities = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Amenity)]
    return jsonify(amenities)

@amenity_bp.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = data_manager.get(amenity_id, Amenity)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    for key, value in data.items():
        setattr(amenity, key, value)
