from storage.base_storage import BaseStorage


class KeyValue(BaseStorage):
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]
