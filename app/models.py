from pydantic import BaseModel


class RenderRequest(BaseModel):
    code: str
    language: str
    style: str = "default"
    line_no_type: str = ""
