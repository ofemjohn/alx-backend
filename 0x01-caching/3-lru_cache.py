#!/usr/bin/python3
""" 3-lru_cache.py """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # if the key already exists, move it to the end of the list
        if key in self.cache_data:
            self.order.remove(key)
        # otherwise, if the cache is full, evict the least recently used item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.order.pop(0)
            del self.cache_data[lru]
            print("DISCARD: {}".format(lru))

        # add the new key to the end of the list and update the cache
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        ''' move the key to the end of the list'''
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
