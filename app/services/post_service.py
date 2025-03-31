from cachetools import TTLCache

# In-memory cache (5 min expiry)
cache = TTLCache(maxsize=100, ttl=300)

def cache_posts(user_id: int, posts):
    """Caches user posts."""
    cache[user_id] = posts

def get_cached_posts(user_id: int):
    """Gets cached posts if available."""
    return cache.get(user_id)
