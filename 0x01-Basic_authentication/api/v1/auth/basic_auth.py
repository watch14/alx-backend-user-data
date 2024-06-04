#!/usr/bin/env python3
"""
Basic Auth class
"""

from models.user import User
from .auth import Auth
import base64
from typing import Tuple, TypeVar


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
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
                self, decoded_base64_authorization_header: str
                ) -> Tuple[str, str]:

        """ returns the user email and password from the Base64 """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        user_info = decoded_base64_authorization_header.split(":", 1)
        if len(user_info) != 2:
            return None, None

        email, password = user_info
        return email, password

    def user_object_from_credentials(
                self, user_email: str, user_pwd: str) -> TypeVar('User'):

        """ returns the User instance based on his email and password """
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User """

        auth_header = self.authorization_header(request)
        base_header = self.extract_base64_authorization_header(auth_header)
        decode_header = self.decode_base64_authorization_header(base_header)
        email, paswd = self.extract_user_credentials(decode_header)

        user = self.user_object_from_credentials(email, paswd)
        return user
