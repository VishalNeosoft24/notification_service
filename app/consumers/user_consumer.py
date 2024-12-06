from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.config import SessionLocal
from app.models.notification import Notification
from app.routers.notification_routes import send_notification_to_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class NotificationConsumer:
    """Notification Consumer to process and handle notifications."""

    def __init__(self):
        pass

    async def create_user_notification(self, user_id, message, operation):
        """
        Create a notification for a user in the database and
        trigger a real-time notification.
        Args:
            user_id (int): ID of the user.
            message (str): Notification message.
            operation (str): Operation type.
        """
        with SessionLocal() as db:
            notification = Notification(
                user_id=user_id,
                message=message,
                status="unread",
                operation=operation,
            )
            db.add(notification)
            db.commit()
            db.refresh(notification)

        await send_notification_to_user(user_id, message)

    async def process_notification_data(self, data):
        """
        Process incoming notification data.
        Args:
            data (dict): Notification data payload.
        """
        try:
            if data["operation"] == "user_register":
                await self.user_register(data=data)
        except KeyError as e:
            print(f"Missing required field in message: {e}")

    async def user_register(self, data):
        """
        Handle user registration notification.
        Args:
            data (dict): Notification data for user registration.
        """
        try:
            message = "New user registered successfully"
            user_id = data.get("user_id")
            operation = data.get("operation")

            await self.create_user_notification(user_id, message, operation)
        except Exception as e:
            raise HTTPException(
                status_code=404, detail=f"Error processing message: {e}"
            )
