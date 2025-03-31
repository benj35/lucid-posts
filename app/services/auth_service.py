from sqlalchemy.orm import Session
from app.models.user_model import User
from passlib.context import CryptContext

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def create_user(email: str, password: str, db: Session):
        """
        Creates a new user with a hashed password.
        Args:
            email (str): The user's email.
            password (str): The user's password.
            db (Session): The database session.
        Returns:
            The created user object.
        """
        hashed_password = pwd_context.hash(password)
        user = User(email=email, password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def authenticate_user(email: str, password: str, db: Session):
        """
        Authenticates a user by verifying their email and password.
        Args:
            email (str): The user's email.
            password (str): The user's password.
            db (Session): The database session.
        Returns:
            The authenticated user object or None if authentication fails.
        """
        user = db.query(User).filter(User.email == email).first()
        if user and pwd_context.verify(password, user.password):
            return user
        return None
