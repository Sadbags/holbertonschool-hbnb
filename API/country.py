from flask import Blueprint, request, jsonify, abort, Blueprint
from country import Country
from Persistence.DataManager import DataManager

country_bp = Blueprint('country', __name__)
data_manager = DataManager()

# Ruta para crear un nuevo país
@country_bp.route('/', methods=['POST'])
def create_country():
    data = request.get_json()
    country = Country(name=data['name'], area_code=data['area_code'])
    data_manager.save(country)
    return jsonify({'id': str(country.id)}), 201

# Ruta para obtener la lista de todos los países
@country_bp.route('/', methods=['GET'])
def get_countries():
    countries = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Country)]
    return jsonify(countries)

# Ruta para obtener los detalles de un país específico por su ID
@country_bp.route('/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(country_id, Country)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.__dict__)

# Ruta para actualizar la información de un país existente
@country_bp.route('/<country_id>', methods=['PUT'])
def update_country(country_id):
    data = request.get_json()
    country = data_manager.get(country_id, Country)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    for key, value in data.items():
        setattr(country, key, value)
    country.save()
    data_manager.update(country)
    return jsonify({'id': str(country.id)}), 200

# Ruta para eliminar un país específico por su ID
@country_bp.route('/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    country = data_manager.get(country_id, Country)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    data_manager.delete(country_id, Country)
    return '', 204
