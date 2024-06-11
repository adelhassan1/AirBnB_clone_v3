#!/usr/bin/python3

from flask import Flask, jsonify
import storage from models
import app_views from api.v1.views

app = Flask(__name__)
app.register_blueprint(app_views)
def close_strorage(exception):
    storage.close()

if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)

@app.errorhandler(404)
def handle_error_not_found_error(e):
    return jsonify({"error": "Not found"}), 404
