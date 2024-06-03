#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv('AUTH_TYPE', 'auth')
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Request unauthorized """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def not_allowed(error) -> str:
    """ Not allowed to access """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def bef_req():
    """ Before request handler """
    exclu_paths = ['/api/v1/status/',
                   '/api/v1/unauthorized/',
                   '/api/v1/forbidden/']

    if auth.require_auth(request.path, exclu_paths):

        if auth.authorization_header(request) is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
