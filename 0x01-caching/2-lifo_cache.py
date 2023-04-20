#!/usr/bin/python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.last_key = []

    def put(self, key, item):
        """ Assign to the dictionary, LIFO algorithm, add element """
        if not key or not item:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.last_key))
            self.cache_data.pop(self.last_key)
        self.last_key = key

    def get(self, key):
        """ Return the value linked """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
