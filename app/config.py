import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Settings:
    """Settings for RabbitMQ and Database."""

    RABBIT_MQ_HOST: str = os.getenv("RABBIT_MQ_HOST", "localhost")
    RABBIT_MQ_QUEUE: str = os.getenv("RABBIT_MQ_QUEUE", "notification_queue")
    RABBIT_MQ_URL: str = os.getenv("RABBIT_MQ_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    BASE_URL: str = os.getenv("BASE_URL")
    MAILTRAP_SMTP_HOST = os.getenv("MAILTRAP_SMTP_HOST")
    MAILTRAP_SMTP_PORT = os.getenv("MAILTRAP_SMTP_PORT")
    MAILTRAP_SMTP_USER = os.getenv("MAILTRAP_SMTP_USER")
    MAILTRAP_SMTP_PASSWORD = os.getenv("MAILTRAP_SMTP_PASSWORD")
    FROM_EMAIL = os.getenv("FROM_EMAIL")
    TO_EMAIL = os.getenv("TO_EMAIL")


# Instantiate Settings
settings = Settings()

# Check if DATABASE_URL is provided
if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create SQLAlchemy Engine
engine = create_engine(settings.DATABASE_URL)

# Create a Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for Models
Base = declarative_base()

db = SessionLocal()
