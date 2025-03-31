from cachetools import TTLCache

# In-memory cache with a maximum size of 100 and a time-to-live of 5 minutes
cache = TTLCache(maxsize=100, ttl=300)

def cache_posts(user_id: int, posts):
    """
    Caches the posts of a specific user.
    Args:
        user_id (int): The ID of the user.
        posts: The posts to be cached.
    """
    cache[user_id] = posts

def get_cached_posts(user_id: int):
    """
    Retrieves cached posts for a specific user if available.
    Args:
        user_id (int): The ID of the user.
    Returns:
        Cached posts or None if not available.
    """
    return cache.get(user_id)
