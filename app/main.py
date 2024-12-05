from fastapi import FastAPI, WebSocket, WebSocketDisconnect, BackgroundTasks
from typing import Dict
from app.services.rabbitmq_consumer import start_consuming
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    print("App is starting up...")
    consumer_task = asyncio.create_task(
        start_consuming()
    )  # Start RabbitMQ consumer as a background task

    yield

    # Shutdown tasks
    print("App is shutting down...")
    consumer_task.cancel()  # Stop the RabbitMQ consumer task
    try:
        await consumer_task
    except asyncio.CancelledError:
        print("RabbitMQ consumer stopped gracefully.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "FastAPI RabbitMQ Consumer is running"}


@app.post("/start-consumer/")
async def start_background_consumer(background_tasks: BackgroundTasks):
    """Start the RabbitMQ message consumer in the background"""
    background_tasks.add_task(start_consuming)
    return {"message": "Started RabbitMQ consumer in background"}


# Dictionary to store WebSocket connections by user ID
active_connections: Dict[str, WebSocket] = {}


# WebSocket route for receiving notifications
@app.websocket("/ws/notifications/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    # Accept the WebSocket connection
    await websocket.accept()

    # Store the WebSocket connection for the specific user
    active_connections[user_id] = websocket
    print(f"User {user_id} connected.")

    try:
        while True:
            # Wait for a message from the client (if needed)
            data = await websocket.receive_text()
            print(f"Received data from {user_id}: {data}")
    except WebSocketDisconnect:
        # Handle disconnections
        active_connections.pop(user_id, None)
        print(f"User {user_id} disconnected")


# Function to send a notification to a specific user
async def send_notification_to_user(user_id: int, message: str):
    connection = active_connections.get(user_id)
    if connection:
        try:
            await connection.send_text(message)
        except:
            # Handle the case where the connection might have closed
            active_connections.pop(user_id, None)
            print(f"Failed to send message to user {user_id}")
    else:
        print(f"No active connection for user {user_id}")
