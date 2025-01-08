import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pika

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


def send_email(to_email: str, subject: str, body: str):
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = settings.FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the email body
    msg.attach(MIMEText(body, "plain"))

    # Connect to the Mailtrap SMTP server
    try:
        with smtplib.SMTP(
            settings.MAILTRAP_SMTP_HOST, settings.MAILTRAP_SMTP_PORT
        ) as server:
            server.starttls()  # Secure the connection
            server.login(
                settings.MAILTRAP_SMTP_USER, settings.MAILTRAP_SMTP_PASSWORD
            )  # Login to your Mailtrap account
            text = msg.as_string()
            server.sendmail(settings.FROM_EMAIL, to_email, text)  # Send the email
            print(f"Email sent to {to_email}!")
    except Exception as e:
        print(f"Error sending email: {e}")
