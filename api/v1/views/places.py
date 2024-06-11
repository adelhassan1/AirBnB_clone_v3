#!/usr/bin/python3
from flask import Flask, jsonify, request
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.city import City
from models.user import User

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_city_places(city_id):
    """
    return a list to all the cities
    """
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    places = city.places
    return jsonify({place.to_dict() for place in places])
@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """
    return a spacific place object
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    return jsonify(place.to_dict())
@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """
    delete place with spacific id
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    storage.delete(place)
    storage.save()
    storage.jsonify({}), 200

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(place_id):
    """
    create a new place with spacific id
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"}), 404
    if "name" not in data:
        return jsonify({"error": "Not a Json"}), 404
    new_place = Place(**data)
    new_place.save()
    return jsonify(new_place.to_dict()), 201
@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """
    update the place with spacific id
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"}), 404
    for key, value  in data.items():
        if key no in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)
    place.save()
    return place.jsonify(place.to_dict()), 200
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import states, cities, amenities, users, places
