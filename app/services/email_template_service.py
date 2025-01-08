from app.config import db
from app.models.email_templates import EmailTemplate
from app.schemas.email_schema import EmailTemplateCreate


class EmailTemplateCrud:
    @staticmethod
    def create_email_template(email_template: EmailTemplateCreate):
        """Create a new email template and save it to the database."""
        try:
            new_email_template = EmailTemplate(
                template_name=email_template.template_name,
                template_html=email_template.template_html,
            )
            db.add(new_email_template)
            db.commit()
            db.refresh(new_email_template)
            return {"message": "New Email Template is created"}
        except Exception as e:
            db.rollback()  # Rollback in case of any error
            raise Exception(f"Error creating email template: {e}")
