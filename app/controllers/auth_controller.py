import jwt
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.auth_service import AuthService
from app.schemas.auth_schema import SignupRequest, LoginRequest
from app.middlewares.auth_middleware import SECRET_KEY

class AuthController:
    @staticmethod
    def signup(user_data: SignupRequest, db: Session):
        """Handles user signup."""
        user = AuthService.create_user(user_data.email, user_data.password, db)
        return {"message": "User created"}

    @staticmethod
    def login(user_data: LoginRequest, db: Session):
        """Handles user login."""
        user = AuthService.authenticate_user(user_data.email, user_data.password, db)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")
        return {"token": token}
