#!/usr/bin/python3

from models import storage
from api.v1.views import app_views

"""
    endpoint that retrieves the number of each objects by type
"""
def get_status():
    stats = {
            amenities: storage.count('Amenity'),
            cities: storage.count('City'),
            places: storage.count('Place'),
            reviews: storage.count('Review'),
            states: storage.count('State'),
            users: storage.count('User')
            }
    return json(stats), 200
