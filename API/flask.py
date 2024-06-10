from flask import Flask
from user import user_bp
from place import place_bp
from review import review_bp
from amenity import amenity_bp
from country import country_bp
from city import city_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(place_bp, url_prefix='/places')
app.register_blueprint(review_bp, url_prefix='/reviews')
app.register_blueprint(amenity_bp, url_prefix='/amenities')
app.register_blueprint(country_bp, url_prefix='/countries')
app.register_blueprint(city_bp, url_prefix='/cities')

if __name__ == '__main__':
    app.run(debug=True)
