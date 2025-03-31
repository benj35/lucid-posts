from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.controllers.post_controller import create_post, get_user_posts, delete_post
from app.middlewares.auth_middleware import get_current_user
from app.schemas.post_schema import PostCreate
from app.services.post_service import cache_posts, get_cached_posts

router = APIRouter()

@router.post("/")
def add_post(post_data: PostCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    """
    Adds a new post for the authenticated user.
    Args:
        post_data (PostCreate): The post data.
        db (Session): The database session.
        user: The authenticated user.
    Returns:
        The ID of the created post.
    """
    post = create_post(db, post_data, user.id)
    return {"postID": post.id}

@router.get("/")
def fetch_posts(db: Session = Depends(get_db), user=Depends(get_current_user)):
    """
    Fetches all posts for the authenticated user.
    Uses cached posts if available, otherwise fetches from the database.
    Args:
        db (Session): The database session.
        user: The authenticated user.
    Returns:
        A list of posts.
    """
    cached = get_cached_posts(user.id)
    if cached:
        return cached
    posts = get_user_posts(db, user.id)
    cache_posts(user.id, posts)
    return posts

@router.delete("/{post_id}")
def remove_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    """
    Deletes a specific post for the authenticated user.
    Args:
        post_id (int): The ID of the post to delete.
        db (Session): The database session.
        user: The authenticated user.
    Returns:
        A success message.
    """
    return delete_post(db, post_id, user.id)
