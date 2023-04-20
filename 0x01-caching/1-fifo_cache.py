#!/usr/bin/python3
""" Inherited module from BaseCaching module.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    and is a caching system using the FIFO algorithm
    """
    def __init__(self):
        '''initialize'''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed_key = self.keys.pop(0)
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''method get the key from class'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data
