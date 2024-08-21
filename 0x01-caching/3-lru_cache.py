#!/usr/bin/env python3
"""
Least Recently Used replacement policy
"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """
    remove the data that hasn't been used in a long time
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.cached_at = {}

    def put(self, key, item):
        """
        assign key:item to self.cache_data
        if key or item empty do nothing
        DISCARD the least Recently used item if cache exceed set max
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cached_at[key] = datetime.utcnow()

        # check if the cache exceed limit and remove the least recently used
        least = min(self.cached_at, key=self.cached_at.get)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[least]
            del self.cached_at[least]

            print(f"DISCARD: {least}")

    def get(self, key):
        """
        get item associated with key
        """
        if key and key in self.cache_data.keys():
            self.cached_at[key] = datetime.utcnow()
            return self.cache_data[key]

        return None
