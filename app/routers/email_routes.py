# Router for API endpoints
from fastapi import APIRouter, BackgroundTasks

from app.schemas.email_schema import EmailRequest, EmailTemplateCreate
from app.services.email_template_service import EmailTemplateCrud
from app.utils.rabbitmq_utils import send_email

email_router = APIRouter()


@email_router.post("/send-email/")
async def send_email_endpoint(
    email_request: EmailRequest, background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_email, email_request.to_email, email_request.subject, email_request.body
    )
    return {"message": "Email is being sent in the background."}


@email_router.post("/create-email-template")
async def create_email_template(email_template: EmailTemplateCreate):
    return EmailTemplateCrud.create_email_template(email_template)
