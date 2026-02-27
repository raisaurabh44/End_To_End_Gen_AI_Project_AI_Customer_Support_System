import os
import redis 
from app.config import REDIS_HOST, CACHE_TTL

class Cache:
    def __init__(self):
        redis_url = os.getenv('REDIS_URL')
        if not redis_url:
            raise ValueError("REDIS_URL not found in environment variables")
        self.client = redis.from_url(redis_url)
        
    def get(self, key):
        val = self.client.get(key)
        return val if val is not None else None
    
    def set(self, key, value, ttl=CACHE_TTL):
        self.client.setex(key, ttl, value)
    
    