#!/usr/bin/env python3
"""
caching system FIFOCache that inherits from BaseCaching
First Data to be recored is the First Data Removed
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Queue - first in first out
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        assign to dictionary key:item
        if key | item is None do nothing
        if the number of items in cache_data > BaseCaching.MAX_ITEMS:
            discard the first input item
            print DISCARD with key discarded
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)

        self.cache_data[key] = item
        self.cache_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest = self.cache_order.pop(0)  # the first item in list
            del self.cache_data[oldest]
            print(f"DISCARD: {oldest}")

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        if key is None or doesn't exist, return None
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
