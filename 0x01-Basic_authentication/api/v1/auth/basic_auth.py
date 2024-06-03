#!/usr/bin/env python3
"""
Basic Auth class
"""

from .auth import Auth


class BasicAuth(Auth):
    """ inherit from Auth class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ BasicAuth that returns the Base64 """
        if authorization_header is None :
            return None
        
        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]
