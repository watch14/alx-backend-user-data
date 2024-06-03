#!/usr/bin/env python3
"""
Basic Auth class
"""

from .auth import Auth
import base64


class BasicAuth(Auth):
    """ inherit from Auth class """
    def extract_base64_authorization_header(
                self, authorization_header: str) -> str:

        """ BasicAuth that returns the Base64 """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
                self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except base64.binascii.Error:
            return None
