#!/usr/bin/python3
"""
MRU Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_keys.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.mru_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_keys.remove(key)
        self.mru_keys.append(key)
        return self.cache_data[key]
