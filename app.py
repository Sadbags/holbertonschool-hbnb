from flask import Flask
from API.user_endpoints import user_bp
from API.place_endpoints import place_bp
from API.review_endpoints import review_bp
from API.amenity_endpoints import amenity_bp
from API.country_endpoints import country_bp

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to api'

app.register_blueprint(user_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(amenity_bp)
app.register_blueprint(country_bp)

if __name__ == '__main__':
    app.run(debug=True)
