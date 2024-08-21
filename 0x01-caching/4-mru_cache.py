#!/usr/bin/env python3
"""
Most Recently Used replacement policy
"""
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
    """
    remove the data that has just been recorded
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
        DISCARD the Most Recently used item if cache exceed set max
        """

        if key is None or item is None:
            return

        # check if the cache exceed limit and remove the most recently used

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most = max(self.cached_at, key=self.cached_at.get)
            del self.cache_data[most]
            del self.cached_at[most]

            print(f"DISCARD: {most}")

        self.cache_data[key] = item
        self.cached_at[key] = datetime.utcnow()

    def get(self, key):
        """
        get item associated with key
        """
        if key and key in self.cache_data.keys():
            self.cached_at[key] = datetime.utcnow()
            return self.cache_data[key]

        return None
