from pydantic import BaseModel


class EmailRequest(BaseModel):
    to_email: str
    subject: str
    body: str


class EmailTemplateCreate(BaseModel):
    template_name: str
    template_html: str

    class Config:
        orm_mode = True
