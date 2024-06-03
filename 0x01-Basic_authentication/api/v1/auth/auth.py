#!/usr/bin/env python3
"""
Auth class
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        returns False - path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header
         that returns None - request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """  current_user
        returns None - request
        """
        return None
