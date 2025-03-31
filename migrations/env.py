# Importing the Base class and engine from the database module
from app.db.database import Base, engine

# Setting the target metadata for Alembic migrations
target_metadata = Base.metadata
