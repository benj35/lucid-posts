from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth_schema import SignupRequest, LoginRequest
from app.controllers.auth_controller import AuthController

router = APIRouter()

@router.post("/signup")
def signup(user_data: SignupRequest, db: Session = Depends(get_db)):
    return AuthController.signup(user_data, db)

@router.post("/login")
def login(user_data: LoginRequest, db: Session = Depends(get_db)):
    return AuthController.login(user_data, db)
