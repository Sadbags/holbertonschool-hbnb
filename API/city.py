from flask import Blueprint, request, jsonify, abort, Blueprint
from city import City
from country import Country
from Persistence.DataManager import DataManager

city_bp = Blueprint('city', __name__)
data_manager = DataManager()

# Ruta para crear una nueva ciudad
@city_bp.route('/', methods=['POST'])
def create_city():
    data = request.get_json()
    country = next((obj for obj in data_manager.storage.objects.values() if isinstance(obj, Country) and obj.area_code == data['country_code']), None)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    
    city = City(name=data['name'], country=country)
    data_manager.save(city)
    return jsonify({'id': str(city.id)}), 201

# Ruta para obtener la lista de todas las ciudades
@city_bp.route('/', methods=['GET'])
def get_cities():
    cities = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, City)]
    return jsonify(cities)

# Ruta para obtener los detalles de una ciudad específica por su ID
@city_bp.route('/<city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, City)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.__dict__)

# Ruta para actualizar la información de una ciudad existente
@city_bp.route('/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    city = data_manager.get(city_id, City)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    for key, value in data.items():
        setattr(city, key, value)
    city.save()
    data_manager.update(city)
    return jsonify({'id': str(city.id)}), 200

# Ruta para eliminar una ciudad específica por su ID
@city_bp.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = data_manager.get(city_id, City)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    data_manager.delete(city_id, City)
    return '', 204
