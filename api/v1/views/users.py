#!/usr/bin/python3
from flask import Flask, jsonify, request
from models import storage
from api.v1.views import app_views
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_user():
    """
    return of all users objects
    """
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    return all userss id
    """
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    deletes all the users_id
    """
    user = storage.get(User, user_id)
    if not user:
         return jsonify({"error": "Not found"}), 404
     storage.deletes(user)
     user.save()
     return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    create a new user
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"}), 404
    if "name" not in data:
        return jsonify({"error": "Not a Json"}), 404
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    update the user
    """
    user = storage.get(User, user_id)
    if not user:
         return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a Json"}), 404
    for key, value in data.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    user.save()
    return user.jsonify(user.to_dict()), 200

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import states, cities, amenities, users
