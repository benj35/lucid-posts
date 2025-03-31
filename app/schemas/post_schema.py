from pydantic import BaseModel

class PostRequest(BaseModel):
    text: str
