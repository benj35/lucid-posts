from sqlalchemy.orm import Session
from app.models.user_model import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def create_user(email: str, password: str, db: Session):
        hashed_password = pwd_context.hash(password)
        user = User(email=email, password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def authenticate_user(email: str, password: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if user and pwd_context.verify(password, user.password):
            return user
        return None
