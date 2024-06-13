from flask import Blueprint, request, jsonify, abort, Blueprint
from review import Review
from user import User
from place import Place
from Persistence.DataManager import DataManager

review_bp = Blueprint('review', __name__)
data_manager = DataManager()

# Ruta para crear una nueva reseña para un lugar específico
@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    user = data_manager.get(data['user_id'], User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404

    if user.id == place.owner.id:
        return jsonify({'error': 'Host cannot review their own place'}), 400

    if not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    review = Review(
        rating=data['rating'],
        content=data['content'],
        author=user,
        place=place
    )
    data_manager.save(review)
    return jsonify({'id': str(review.id)}), 201

# Ruta para obtener todas las reseñas escritas por un usuario específico
@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user = data_manager.get(user_id, User)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    reviews = [review.__dict__ for review in data_manager.storage.objects.values() if isinstance(review, Review) and review.author.id == user.id]
    return jsonify(reviews)

# Ruta para obtener todas las reseñas de un lugar específico
@review_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    place = data_manager.get(place_id, Place)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    reviews = [review.__dict__ for review in data_manager.storage.objects.values() if isinstance(review, Review) and review.place.id == place.id]
    return jsonify(reviews)

# Ruta para obtener los detalles de una reseña específica por su ID
@review_bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.__dict__)

# Ruta para actualizar la información de una reseña existente
@review_bp.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    if 'rating' in data and not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    for key, value in data.items():
        setattr(review, key, value)
    review.save()
    data_manager.update(review)
    return jsonify({'id': str(review.id)}), 200

# Ruta para eliminar una reseña específica por su ID
@review_bp.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get(review_id, Review)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    data_manager.delete(review_id, Review)
    return '', 204
