from flask import Flask, Blueprint, request, jsonify, abort
from Model.country import Country
from Persistence.DataManager import DataManager

app = Flask(__name__)
country_bp = Blueprint('country_bp', __name__, url_prefix='/countries')
data_manager = DataManager(directory='data')  # Proveer un directorio válido

@country_bp.route('/', methods=['POST'])
def create_country():
    data = request.get_json()
    country = Country(name=data['name'], code=data['code'])
    data_manager.save(country)
    return jsonify({'id': country.id, 'name': country.name}), 201

@country_bp.route('/', methods=['GET'])
def get_countries():
    countries = [country.__dict__ for country in data_manager.storage.values() if isinstance(country, Country)]
    return jsonify(countries), 200

@country_bp.route('/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(country_id, Country)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.__dict__), 200

@country_bp.route('/<country_id>', methods=['PUT'])
def update_country(country_id):
    data = request.get_json()
    country = data_manager.get(country_id, Country)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    for key, value in data.items():
        setattr(country, key, value)
    country.save()
    data_manager.update(country)
    return jsonify(country.__dict__), 200

@country_bp.route('/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    country = data_manager.get(country_id, Country)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    data_manager.delete(country_id, Country)
    return '', 204

app.register_blueprint(country_bp)

if __name__ == '__main__':
    app.run(debug=True)
