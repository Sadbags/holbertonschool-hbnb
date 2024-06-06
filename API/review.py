from flask import Blueprint, request, jsonify
from review import Review
from user import User
from place import Place
from Persistence.DataManager import DataManager

review_bp = Blueprint('review', __name__)
data_manager = DataManager()

@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    user = data_manager.get(data['user_id'], User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404

    review = Review(
        rating=data['rating'],
        content=data['content'],
        author=user,
        place=place
    )
    data_manager.save(review)
    return jsonify({'id': str(review.id)}), 201

@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    reviews = [review.__dict__ for review in data_manager.storage.objects.values() if isinstance(review, Review) and review.author.id == user.id]
    return jsonify(reviews)

@review_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    reviews = [review.__dict__ for review in data_manager.storage.objects.values() if isinstance(review, Review) and review.place.id == place.id]
    return jsonify(reviews)

@review_bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.__dict__)

@review_bp.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    for key, value in data.items():
        setattr(review, key, value)
    review.save()
    data_manager.update(review)
    return jsonify({'id': str(review.id)}), 200

@review_bp.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    data_manager.delete(review_id, Review)
    return '', 204
