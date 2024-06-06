from flask import Blueprint, request, jsonify
from place import Place
from user import User
from city import City
from Persistence.DataManager import DataManager

place_bp = Blueprint('place', __name__)
data_manager = DataManager()

@place_bp.route('/', methods=['POST'])
def create_place():
    data = request.get_json()
    user = data_manager.get(data['host_id'], User)
    if user is None:
        return jsonify({'error': 'Host not found'}), 404

    city = data_manager.get(data['city_id'], City)
    if city is None:
        return jsonify({'error': 'City not found'}), 404

    place = Place(
        name=data['name'],
        description=data['description'],
        address=data['address'],
        city=city,
        owner=user,
        price_per_night=data['price_per_night'],
    )
    data_manager.save(place)
    return jsonify({'id': str(place.id)}), 201

@place_bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.__dict__)

@place_bp.route('/', methods=['GET'])
def get_places():
    places = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Place)]
    return jsonify(places)

@place_bp.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    for key, value in data.items():
        setattr(place, key, value)
    place.save()
    data_manager.update(place)
    return jsonify({'id': str(place.id)}), 200

@place_bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    data_manager.delete(place_id, Place)
    return '', 204
