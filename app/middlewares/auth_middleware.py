from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.db.database import get_db
from app.models.user_model import User
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Secret key for JWT token validation
SECRET_KEY = os.getenv("SECRET_KEY")
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    """
    Extracts and validates the JWT token to authenticate the user.
    Args:
        credentials (HTTPAuthorizationCredentials): The authorization credentials.
        db (Session): The database session.
    Returns:
        The authenticated user object.
    Raises:
        HTTPException: If the token is invalid or expired.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = db.query(User).filter(User.id == payload["user_id"]).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
