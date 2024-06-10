from flask import Blueprint, request, jsonify
from place import Place
from user import User
from city import City
from amenity import Amenity
from Persistence.DataManager import DataManager

place_bp = Blueprint('place', __name__)
data_manager = DataManager()

# Ruta para crear un nuevo lugar
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
        location=data['location'],
        owner=user,
        description=data.get('description', ''),
        address=data.get('address', ''),
        city=city,
        price_per_night=data.get('price_per_night', 0)
    )

    for amenity_id in data.get('amenity_ids', []):
        amenity = data_manager.get(amenity_id, Amenity)
        if amenity:
            place.add_amenity(amenity)

    data_manager.save(place)
    return jsonify({'id': str(place.id)}), 201

# Ruta para obtener la lista de todos los lugares
@place_bp.route('/', methods=['GET'])
def get_places():
    places = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Place)]
    return jsonify(places)

# Ruta para obtener los detalles de un lugar específico por su ID
@place_bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.__dict__)

# Ruta para actualizar la información de un lugar existente
@place_bp.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404

    if 'host_id' in data:
        user = data_manager.get(data['host_id'], User)
        if user is None:
            return jsonify({'error': 'Host not found'}), 404
        place.owner = user

    if 'city_id' in data:
        city = data_manager.get(data['city_id'], City)
        if city is None:
            return jsonify({'error': 'City not found'}), 404
        place.city = city

    for key, value in data.items():
        if key != 'amenity_ids':
            setattr(place, key, value)

    if 'amenity_ids' in data:
        place.amenities = []
        for amenity_id in data['amenity_ids']:
            amenity = data_manager.get(amenity_id, Amenity)
            if amenity:
                place.add_amenity(amenity)

    place.save()
    data_manager.update(place)
    return jsonify({'id': str(place.id)}), 200

# Ruta para eliminar un lugar específico por su ID
@place_bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    data_manager.delete(place_id, Place)
    return '', 204
