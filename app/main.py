from redis.redis import Redis
from env.env import environment as env
from storage.key_value import KeyValue

if __name__ == "__main__":
    with Redis(KeyValue(), env.get("HOST"), env.get("PORT")) as redis:
        redis.run()
