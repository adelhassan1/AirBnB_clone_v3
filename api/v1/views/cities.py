#!/usr/bin/python3
from flask import Flask, request, jsonify
from models import storage
from app.v1.views import app_views
from models.city import City
from models.state import State

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_state_city(state_id):
    """
    return list for all cities
    """
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "Not Found"}), 404
    Cities = state.cities
    return jsonify([city.to_dict() for city in cities])
@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)

def get_city(City_id):
    """
    return specific city object
    """
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def deletes_city(city_id):
    """
    deletes city objects
    """
    City = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not Found"}), 404
    storage.delete(city)
    storage.save()
    return jsonify({), 200

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """
    create city associated with city
    """
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    new_city = City(**data)
    new_city.state.id = state_id
    new_city.save()
    return jsonify(new_city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """
    update city object
    """
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"})
    for key, value in data.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import states, cities
        

