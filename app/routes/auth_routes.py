from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth_schema import SignupRequest, LoginRequest
from app.controllers.auth_controller import AuthController

router = APIRouter()

@router.post("/signup")
def signup(user_data: SignupRequest, db: Session = Depends(get_db)):
    """
    Handles user signup.
    Args:
        user_data (SignupRequest): The signup data.
        db (Session): The database session.
    Returns:
        A success message.
    """
    return AuthController.signup(user_data, db)

@router.post("/login")
def login(user_data: LoginRequest, db: Session = Depends(get_db)):
    """
    Handles user login.
    Args:
        user_data (LoginRequest): The login data.
        db (Session): The database session.
    Returns:
        A JWT token if login is successful.
    """
    return AuthController.login(user_data, db)
