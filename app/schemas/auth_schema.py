from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    """
    Schema for user signup requests.
    Attributes:
        email (EmailStr): The user's email.
        password (str): The user's password.
    """
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    """
    Schema for user login requests.
    Attributes:
        email (EmailStr): The user's email.
        password (str): The user's password.
    """
    email: EmailStr
    password: str
