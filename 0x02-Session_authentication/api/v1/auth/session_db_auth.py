#!/usr/bin/env python3
"""
Sessions in database
"""
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Session Expiration"""

    def create_session(self, user_id=None):
        """create_session"""
        pass

    def user_id_for_session_id(self, session_id=None):
        """ user_id_for_session_id """
        pass

    def destroy_session(self, request=None):
        """ destroy_session """
        pass
