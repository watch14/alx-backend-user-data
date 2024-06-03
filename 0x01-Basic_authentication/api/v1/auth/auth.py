#!/usr/bin/env python3
"""
Auth class
"""

import fnmatch
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        returns False - path
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
         that returns None - request
        """
        if request is not None:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """  current_user
        returns None - request
        """
        return None
