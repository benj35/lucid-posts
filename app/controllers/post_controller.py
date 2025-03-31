from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate
from fastapi import HTTPException

def create_post(db: Session, post_data: PostCreate, user_id: int):
    """
    Creates a new post for a user.
    Args:
        db (Session): The database session.
        post_data (PostCreate): The post data.
        user_id (int): The ID of the user creating the post.
    Returns:
        The created post object.
    """
    post = Post(text=post_data.text, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db: Session, user_id: int):
    """
    Fetches all posts of a specific user.
    Args:
        db (Session): The database session.
        user_id (int): The ID of the user.
    Returns:
        A list of posts.
    """
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    """
    Deletes a specific post of a user.
    Args:
        db (Session): The database session.
        post_id (int): The ID of the post to delete.
        user_id (int): The ID of the user.
    Returns:
        A success message.
    Raises:
        HTTPException: If the post is not found.
    """
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted"}
