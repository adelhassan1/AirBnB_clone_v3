#!/usr/bin/python3

from flask import Flask, jsonify
@app.errorhandler(404)
def handle_error_not_found_error(e):
    return jsonify({"error": "Not found"}), 404
