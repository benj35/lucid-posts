from fastapi import APIRouter
from app.routes.auth_routes import router as auth_router
from app.routes.post_routes import router as post_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(post_router, prefix="/posts", tags=["Posts"])
