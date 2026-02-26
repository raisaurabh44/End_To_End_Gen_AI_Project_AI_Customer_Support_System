import redis 
from app.config import REDIS_HOST, CACHE_TTL

class Cache:
    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
        
    def get(self, key):
        val = self.client.get(key)
        return val if val is not None else None
    
    def set(self, key, value):
        self.client.setex(key, CACHE_TTL, value)
    
    