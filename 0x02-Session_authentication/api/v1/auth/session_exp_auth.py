#!/usr/bin/env python3
"""
session Expiration auth
"""
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session Expiration"""
    def __init__(self):
        """ inint fnc """
        pass

    def create_session(self, user_id=None):
        """create_session"""
        pass

    def user_id_for_session_id(self, session_id=None):
        """ user_id_for_session_id """
        pass
