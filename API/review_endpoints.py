from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required
from Model.review import Review
from Persistence.DataManager import DataManager

review_blueprint = Blueprint('review_blueprint', __name__)
data_manager = DataManager()

@review_blueprint.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    if not request.json or not all(key in request.json for key in ('user_id', 'rating', 'comment')):
        abort(400, description="Missing required fields")

    user_id = request.json['user_id']
    rating = request.json['rating']
    comment = request.json['comment']


    if not (1 <= rating <= 5):
        abort(400, description="Rating must be between 1 and 5")

    review = Review(place_id=place_id, user_id=user_id,
                    rating=rating, comment=comment)
    data_manager.save(review)

    return jsonify(review.to_dict()), 201


@review_blueprint.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    reviews = [review.to_dict() for review in data_manager.storage.get(
        'Review', {}).values() if review.user_id == user_id]
    return jsonify(reviews), 200


@review_blueprint.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    reviews = [review.to_dict() for review in data_manager.storage.get(
        'Review', {}).values() if review.place_id == place_id]
    return jsonify(reviews), 200


@review_blueprint.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, 'Review')
    if not review:
        abort(404, description="Review not found")
    return jsonify(review.to_dict()), 200


@review_blueprint.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    review = data_manager.get(review_id, 'Review')
    if not review:
        abort(404, description="Review not found")

    if not request.json:
        abort(400, description="Missing required fields")

    review.rating = request.json.get('rating', review.rating)
    review.comment = request.json.get('comment', review.comment)

    if not (1 <= review.rating <= 5):
        abort(400, description="Rating must be between 1 and 5")

    data_manager.update(review)
    return jsonify(review.to_dict()), 200


@review_blueprint.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get(review_id, 'Review')
    if not review:
        abort(404, description="Review not found")
    data_manager.delete(review_id, 'Review')
    return '', 204
