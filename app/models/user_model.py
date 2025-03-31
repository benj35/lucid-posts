from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    """
    Represents a user in the database.
    Attributes:
        id (int): The primary key of the user.
        email (str): The user's email.
        password (str): The user's hashed password.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
