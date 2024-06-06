#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv('AUTH_TYPE', 'auth')

if auth_type == 'auth':
    auth = Auth()

elif auth_type == 'basic_auth':
    auth = BasicAuth()

elif auth_type == 'session_auth':
    auth = SessionAuth()


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
    setattr(request, "current_user", auth.current_user(request))
    exclu_paths = ['/api/v1/status/',
                   '/api/v1/unauthorized/',
                   '/api/v1/forbidden/',
                   '/api/v1/auth_session/login/',
                   ]

    if auth.require_auth(request.path, exclu_paths):

        cookies = auth.session_cookie(request)
        if auth.authorization_header(request) is None and cookies is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
