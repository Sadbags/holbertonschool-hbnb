from flask import Flask
from API.user_endpoints import user_bp
from API.place_endpoints import place_bp
from API.review_endpoints import review_bp
from API.amenity_endpoints import amenity_bp
from API.country_endpoints import country_bp
from API.city_endpoints import city_bp

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to api'

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(place_bp, url_prefix='/places')
app.register_blueprint(review_bp, url_prefix='/reviews')
app.register_blueprint(amenity_bp, url_prefix='/amenities')
app.register_blueprint(country_bp, url_prefix='/countries')
app.register_blueprint(city_bp, url_prefix='/cities')

if __name__ == '__main__':
    app.run(debug=True)
