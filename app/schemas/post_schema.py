from pydantic import BaseModel

class PostRequest(BaseModel):
    """
    Schema for creating a new post.
    Attributes:
        text (str): The content of the post.
    """
    text: str
