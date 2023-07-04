import redis
from typing import Any


class RedisService:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.redis_conn = redis.Redis(host=host, port=port, db=db)

    def get_value(self, key: str) -> Any:
        return self.redis_conn.get(key)

    def set_value(self, key: str, value: Any, ex: int = None):
        self.redis_conn.set(key, value, ex=ex)

    def delete_key(self, key: str):
        self.redis_conn.delete(key)
