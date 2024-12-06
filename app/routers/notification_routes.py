from typing import Dict

from fastapi import (
    APIRouter,
    HTTPException,
    Request,
    WebSocket,
    WebSocketDisconnect,
    status,
)
from sqlalchemy import desc

from app.config import db
from app.models.notification import Notification
from app.services.user_service import AuthService

# Router for API endpoints
router = APIRouter()

# auth service to check token
auth_service = AuthService()

# Dictionary to store WebSocket connections by user ID
active_connections: Dict[int, WebSocket] = {}


@router.websocket("/ws/notifications/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    """
    WebSocket endpoint for real-time notifications.
    """
    try:
        # Accept the WebSocket connection
        await websocket.accept()

        # Store the WebSocket connection for the specific user
        active_connections[user_id] = websocket
        print(f"User {user_id} connected via WebSocket.")

        notifications = (
            db.query(Notification)
            .filter(Notification.user_id == user_id)
            .order_by(desc(Notification.created_at))
            .limit(10)
            .all()
        )

        for notification in notifications:
            await websocket.send_text(notification.message)

    except WebSocketDisconnect:
        # Remove the connection when the user disconnects
        active_connections.pop(user_id, None)
        print(f"User {user_id} disconnected from WebSocket.")


async def send_notification_to_user(user_id: int, message: str) -> None:
    """
    Send a real-time notification to a specific user via WebSocket.
    """
    connection = active_connections.get(user_id)
    if connection:
        try:
            await connection.send_text(message)
            print(f"Notification sent to user {user_id}: {message}")
        except Exception as e:
            # Handle WebSocket errors, such as closed connections
            active_connections.pop(user_id, None)
            print(f"Failed to send message to user {user_id}, error: {e}")
    else:
        print(f"No active WebSocket connection for user {user_id}")


@router.get("/get-notification/")
def get_user_specific_notification(request: Request):
    """
    Endpoint to send notifications after token validation.
    """
    try:
        access_token = request.headers.get("Authorization")
        if not access_token:
            # Handle the case where access_token not is provided
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Access token is missing",
            )
        access_token = access_token.split()[1]
        user_id = auth_service.verify_user_token(access_token)
        notifications = (
            db.query(Notification).filter(Notification.user_id == user_id).all()
        )
        return {"message": "Notification get", "data": notifications}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
