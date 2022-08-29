from datetime import datetime, timedelta

from storage.base_storage import BaseStorage


class KeyValue(BaseStorage):
    def __init__(self):
        self.data = {}

    def set(self, key, value, ttl=None):
        ts = None
        if ttl:
            expiry = datetime.utcnow() + timedelta(milliseconds=ttl)
            ts = expiry
        self.data[key] = (value, ts)

    def get(self, key):
        value, expiry_ts = self.data[key]
        if expiry_ts and datetime.utcnow().timestamp() > expiry_ts:
            del self.data[key]
            return None
        return value
