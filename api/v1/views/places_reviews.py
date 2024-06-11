#!/usr/bin/python3

from flask import Flask, jsonify, request
from models import storage
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.user import User
@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_places_revies(place_id):
    """
    retuen a list of review places objects
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    reviews = places.review
    return jsonify([reviews.to_dict for review in reviews()])

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """
    reviews for spacifci object
    """
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({"error": "Not found"}), 404
    return jsonify(review.to_dict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """
    delete reviews
    """
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({"error": "Not found"}), 404
    storage.delete(review)
    storage.save()
    return jsonify({}), 200
@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """
    create a new review
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    data = request.json()
    if not data:
        return jsonify({"error": "Not a Json"}), 400
    if "user_id" not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if "text" not in data:
        return jsonify({"error": "User not found"}), 404
    new_review = Review(**data)
    new_review.place_id = place_id
    new_review.save()
    return jsonify(new_review.to_dict())
@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """
    update the review paced on the id
    """
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"}), 400
    for key, value in data.items():
        if key not in ["id", "user_id", "place_id", "created_at", "updated_at"]:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import states, cities, amenities, users, places, places_reviews
