from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate
from fastapi import HTTPException

def create_post(db: Session, post_data: PostCreate, user_id: int):
    """Creates a new post."""
    post = Post(text=post_data.text, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db: Session, user_id: int):
    """Fetches all posts of a user."""
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    """Deletes a user's post."""
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted"}
