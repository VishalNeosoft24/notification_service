import pika
import json
from app.config import settings


def create_rabbitmq_connection():
    """Create and return a RabbitMQ connection"""
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.RABBITMQ_HOST)
        )

        return connection
    except Exception as e:
        print(f"Error creating RabbitMQ connection: {e}")
        raise


def create_channel(connection):
    """Create and return a RabbitMQ channel"""
    try:
        channel = connection.channel()
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE)
        return channel
    except Exception as e:
        print(f"Error creating RabbitMQ channel: {e}")
        raise
