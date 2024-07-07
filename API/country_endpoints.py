from flask import Blueprint, request, jsonify, abort
from Model.city import City
from Model.country import Country
from Persistence.DataManager import DataManager
from database import db


country_blueprint = Blueprint('country_blueprint', __name__,)
data_manager = DataManager()


@country_blueprint.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([country.to_dict() for country in countries]), 200

# GET a specific country by country code
@country_blueprint.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404, description="Country not found")
    return jsonify(country.to_dict()), 200

# GET cities by country code
@country_blueprint.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404, description="Country not found")

    cities = City.query.filter_by(country_code=country_code).all()
    return jsonify([city.to_dict() for city in cities]), 200

# POST a new city
@country_blueprint.route('/cities', methods=['POST'])
def create_city():
    if not request.json or 'name' not in request.json or 'country_code' not in request.json:
        abort(400, "Missing required fields")

    name = request.json['name']
    country_code = request.json['country_code']

    existing_city = City.query.filter_by(name=name, country_code=country_code).first()
    if existing_city:
        abort(409, "City name already exists in this country")

    city = City(name=name, country_code=country_code)
    db.session.add(city)
    db.session.commit()

    return jsonify({"city_id": city.id, "city": city.to_dict()}), 201

# GET all cities
@country_blueprint.route('/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()
    return jsonify([city.to_dict() for city in cities]), 200

# GET a specific city by city_id
@country_blueprint.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404, description="City not found")
    return jsonify(city.to_dict()), 200

# PUT update a specific city by city_id
@country_blueprint.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404, description="City not found")

    if not request.json:
        abort(400, description="Missing JSON data")

    if 'name' in request.json:
        city.name = request.json['name']

    if 'country_code' in request.json:
        new_country_code = request.json['country_code']

        if not Country.query.filter_by(country_code=new_country_code).first():
            abort(400, description="Invalid country code")

        city.country_code = new_country_code

    db.session.commit()

    return jsonify(city.to_dict()), 200

# DELETE a specific city by city_id
@country_blueprint.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404, description="City not found")

    db.session.delete(city)
    db.session.commit()
    return '', 204