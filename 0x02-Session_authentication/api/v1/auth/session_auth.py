#!/usr/bin/env python3
"""
session Auth class
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ session authorizer """
    user_id_by_session_id  = {}
    def create_session(self, user_id: str = None) -> str:
        """ create session """
        if user_id is None or not isinstance(user_id, str):
            return None

        user_id = uuid.uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)
