import requests
from fastapi import HTTPException

from app.config import settings


class AuthService:
    """Verify token and get user profile"""

    def __init__(self):
        self.BASE_URL = settings.BASE_URL

    def verify_user_token(self, token):
        """
        Get User Profile using valid token.
        Args:
            token (str): access token.
        """
        headers = {"Authorization": f"Bearer {token}"}
        DJANGO_VERIFY_TOKEN_URL = "http://127.0.0.1:8000/api/user/user-profile/"

        response = requests.get(
            DJANGO_VERIFY_TOKEN_URL,
            headers=headers,
        )
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        return response.json()["data"].get("id")
