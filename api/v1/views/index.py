#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['Get'])
def status():
    return jsonify({"status": "OK"})

def get_status():
"""
    endpoint that retrieves the number of each objects by type
"""
    stats = {
            amenities: storage.count('Amenity'),
            cities: storage.count('City'),
            places: storage.count('Place'),
            reviews: storage.count('Review'),
            states: storage.count('State'),
            users: storage.count('User')
            }
    return jsonify(stats), 200
