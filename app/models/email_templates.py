from sqlalchemy import Column, Integer, String, Text

from app.config import Base


class EmailTemplate(Base):
    __tablename__ = "emailtemplates"

    id = Column(Integer, primary_key=True, index=True)
    template_name = Column(String(60), nullable=False)
    template_html = Column(Text, nullable=False)

    def __repr__(self):
        return f"<EmailTemplate(id={self.id}, template_name={self.template_name})>"
