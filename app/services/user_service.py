import requests
from fastapi import HTTPException


class AuthService:
    """Verify token and get user profile"""

    def __init__(self):
        self.DJANGO_VERIFY_TOKEN_URL = "http://127.0.0.1:8000/api/user/user-profile/"

    def verify_user_token(self, token):
        """
        Get User Profile using valid token.
        Args:
            token (str): access token.
        """
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            self.DJANGO_VERIFY_TOKEN_URL,
            headers=headers,
        )
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        return response.json()["data"].get("id")
