from flask import Blueprint, request, jsonify, abort
from Model.review import Review
from Model.user import User
from Model.place import Place
from Persistence.DataManager import DataManager
import re

review_bp = Blueprint('review_bp', __name__)
data_manager = DataManager()

# Helper function to validate rating
def validate_rating(rating):
    return isinstance(rating, int) and 1 <= rating <= 5

# Route to create a new review
@review_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()

    author_id = data.get('author_id')
    place_id = data.get('place_id')
    rating = data.get('rating')
    content = data.get('content')

    if not validate_rating(rating):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    author = data_manager.get(author_id, User)
    place = data_manager.get(place_id, Place)

    if not author or not place:
        return jsonify({'error': 'Invalid author or place ID'}), 400

    if author == place.host:
        return jsonify({'error': 'The host cannot review their own place'}), 400

    review = Review(rating=rating, content=content, author=author, place=place)
    data_manager.save(review)
    return jsonify({'id': str(review.id)}), 201

# Route to get the list of all reviews
@review_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = [obj.__dict__ for obj in data_manager.storage.objects.values() if isinstance(obj, Review)]
    return jsonify(reviews)

# Route to get the details of a specific review by ID
@review_bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.__dict__)

# Route to update an existing review's information
@review_bp.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    if 'rating' in data and not validate_rating(data['rating']):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    for key, value in data.items():
        setattr(review, key, value)
    review.save()
    data_manager.update(review)
    return jsonify({'id': str(review.id)}), 200

# Route to delete a specific review by ID
@review_bp.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    data_manager.delete(review_id, Review)
    return '', 204