from flask import Blueprint, request, jsonify, abort, Blueprint
from country import Country
from city import City
from Persistence.DataManager import DataManager

country_bp = Blueprint('country', __name__)
data_manager = DataManager()


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

# Ruta para obtener todas las ciudades que pertenecen a un país específico
@country_bp.route('/<country_id>/cities', methods=['GET'])
def get_cities_by_country(country_id):
    country = data_manager.get(country_id, Country)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404

    cities = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, City) and obj.country == country]
    return jsonify(cities)
