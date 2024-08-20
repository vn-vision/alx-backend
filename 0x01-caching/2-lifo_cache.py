#!/usr/bin/env python3
"""
LIFOCache inherits from BaseCaching
A cache system where the last input is first output
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Stack - Last in First out
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        assign key:item to self.cache_data
        if key | item is None do nothing
        if self.cache_data > BasicCaching.MAX_ITEMS:
            remove last item input
            print DISCARD: Key
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)

        self.cache_data[key] = item
        self.cache_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest = self.cache_order.pop()
            del self.cache_data[newest]
            print(f"DISCARD: {newest}")

    def get(self, key):
        """
        return self.cache_data linked to key
        if None or doesn't exists return None
        """

        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
