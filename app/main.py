from fastapi import FastAPI
from app.routes.routes import router

# Initialize the FastAPI application
app = FastAPI()

# Include the main router
app.include_router(router)

@app.get("/")
def read_root():
    """
    Root endpoint of the application.
    Returns:
        A welcome message.
    """
    return {"message": "FastAPI MVC Structure For Lucid Posts"}