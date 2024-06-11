#!/usr/bin/python3

from  flask import Flask, jsonify, request
from models import storage
from api.vi.views import app_views
from models.state import State

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_ststus():
    """
    retrun a list of all objects
    """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in States])

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """
    return specific state objects
    """
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "not found"}), 404
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    deletes all states
    """
    state = storage.get(State, state_id)
    if not state:
        return ({"error", "Not Found"}), 404
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    create a new state
    """
    date = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data:
        return jsonify ({"error": "Missing name"}), 400
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201
@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """
    update state object
    """
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify("error": "Not a JSON"}), 400
    for key, value in data.items():
        if "key" not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import states
