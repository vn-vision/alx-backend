#!/usr/bin/env python3
"""
caching system that inherits from BaseCaching
it does not have a limit
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system doesn't have a limit
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        key:value
        if key | item is None, do nothing
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        if key is None | doesn't exist, return None
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
