from base_caching import BaseCaching
""" Inherited module from BaseCaching module.
LRU Caching
"""


class LRUCache(BaseCaching):
    '''caching class'''
    def __init__(self):
        '''initializes'''
        super().__init__()
        self.head = '-'
        self.tail = '='
        self.next = {}
        self.prev = {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        '''handles head and tail'''
        self.next[head] = tail
        self.prev[tail] = head

    def _remove(self, key):
        '''removes key'''
        self.next[self.prev[key]] = self.next[key]
        self.prev[self.next[key]] = self.prev[key]
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        '''add key, value'''
        self.cache_data[key] = item
        self.next[self.prev[self.tail]] = key
        self.prev[key] = self.prev[self.tail]
        self.next[key] = self.tail
        self.prev[self.tail] = key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.next[self.head]
            self._remove(to_discard)
            print("DISCARD: {}".format(to_discard))

    def put(self, key, item):
        '''add key, value'''
        if not key or not item:
            return
        if key in self.cache_data:
            self._remove(key)
        self._add(key, item)

    def get(self, key):
        '''get key'''
        if not key or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self._remove(key)
        self._add(key, value)
        return value
