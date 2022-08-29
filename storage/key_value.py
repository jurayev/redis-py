from datetime import datetime, timedelta

from storage.base_storage import BaseStorage


class KeyValue(BaseStorage):
    def __init__(self):
        self.data = {}

    def set(self, key, value, ttl=3600000):
        expiry = datetime.utcnow() + timedelta(milliseconds=ttl)
        self.data[key] = (value, expiry.timestamp())

    def get(self, key):
        value, expiry_ts = self.data[key]
        if datetime.utcnow().timestamp() > expiry_ts:
            del self.data[key]
            return None
        return value
