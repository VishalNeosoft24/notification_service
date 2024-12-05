import enum
from datetime import datetime

from sqlalchemy import Column, Enum, Integer, String

from app.config import Base


# Define Enum for Notification Status
class NotificationStatus(enum.Enum):
    unread = "unread"
    read = "read"
    dismissed = "dismissed"


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    message = Column(String(255), index=True)
    status = Column(Enum(NotificationStatus), default=NotificationStatus.unread)
    operation = Column(String(255))
    created_at = Column(String(255), default=datetime.now())
