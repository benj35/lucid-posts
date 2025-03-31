from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Post(Base):
    """
    Represents a post in the database.
    Attributes:
        id (int): The primary key of the post.
        text (str): The content of the post.
        user_id (int): The ID of the user who created the post.
        user: The relationship to the User model.
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="posts")
