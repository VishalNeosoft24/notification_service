import asyncio
import json

import aio_pika

from app.config import settings
from app.consumers.user_consumer import NotificationConsumer


async def callback(message: aio_pika.IncomingMessage):
    """Process the message from the queue asynchronously"""
    async with message.process():
        try:
            message_data = json.loads(message.body.decode())

            # Call function to process the message
            notification_consumer = NotificationConsumer()
            await notification_consumer.process_notification_data(message_data)

        except Exception as e:
            print(f"Error processing message: {e}")
            # Optionally, log or handle errors as needed


async def start_consuming():
    """Start consuming messages from the RabbitMQ queue asynchronously"""
    try:
        # Create a connection to RabbitMQ using aio-pika
        connection = await aio_pika.connect_robust(settings.RABBIT_MQ_URL)

        async with connection:
            # Create a channel
            channel = await connection.channel()  # type: aio_pika.Channel
            # Declare the queue if necessary
            queue = await channel.declare_queue(settings.RABBIT_MQ_QUEUE)

            # Start consuming messages
            await queue.consume(callback)
            print(
                f"Waiting for messages in {settings.RABBIT_MQ_QUEUE}. "
                "To exit press CTRL+C."
            )

            # Keep the consumer running
            # This will keep the program running to listen for messages
            await asyncio.Future()

    except Exception as e:
        print(f"Error in consumer: {e}")
