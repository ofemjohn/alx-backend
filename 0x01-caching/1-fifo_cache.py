#!/usr/bin/python3
""" Inherited module from 'BaseCaching' module
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
        self.fifo_rule = []

    def put(self, key, item):
        '''method retrieves key, value'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            fifo_key = self.fifo_rule.pop(0)
            del self.cache_data[fifo_key]
            print('DISCARD: {}'.format(fifo_key))

        self.cache_data[key] = item
        self.fifo_rule.append(key)

    def get(self, key):
        '''method get the key from class'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data
