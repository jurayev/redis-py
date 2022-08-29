from redis.redis import Redis
from env.env import environment as env

if __name__ == "__main__":
    with Redis(env.get("HOST"), env.get("PORT")) as redis:
        redis.run()
