from flask import Flask
from database import db
import os
from flask_jwt_extended import JWTManager
from API.user_endpoints import user_blueprint
from API.place_endpoints import place_blueprint
from API.review_endpoints import review_blueprint
from API.amenity_endpoints import amenity_blueprint
from API.country_endpoints import country_blueprint
from flask_migrate import Migrate

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    JWT_SECRET_KEY = 'super-secret'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


environment_config = DevelopmentConfig if os.environ.get(
    'ENV') == 'development' else ProductionConfig
app.config.from_object(environment_config)

db.init_app(app)
jwt = JWTManager(app)


@app.route('/')
def home():
    return 'Hello, API'


app.register_blueprint(user_blueprint)
app.register_blueprint(country_blueprint)
app.register_blueprint(amenity_blueprint)
app.register_blueprint(place_blueprint)
app.register_blueprint(review_blueprint)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
