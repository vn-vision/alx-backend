#!/usr/bin/env python3
'''
index_range: ttakes two arguments page and page_size
    @page: page number
    @page_size: page size

Return: tuple of ize two containing start index and rend inde
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int,  int]:
    '''
    return tuple of size two
    end index corresponds to range of indexes to return in a list 4 pagination
    '''

    # if a single page has n page size, its index range is n
    # n * page number gives you the last index

    end_index = page * page_size
    start_index = end_index - page_size

    res = (int(start_index), int(end_index))
    return res
