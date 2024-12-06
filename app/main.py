import asyncio
from contextlib import asynccontextmanager

from fastapi import BackgroundTasks, FastAPI

from app.routers.notification_routes import router as notification_router
from app.services.rabbitmq_consumer import start_consuming


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
app.include_router(notification_router)


@app.get("/")
def read_root():
    return {"message": "FastAPI RabbitMQ Consumer is running"}


@app.post("/start-consumer/")
async def start_background_consumer(background_tasks: BackgroundTasks):
    """Start the RabbitMQ message consumer in the background"""
    background_tasks.add_task(start_consuming)
    return {"message": "Started RabbitMQ consumer in background"}
