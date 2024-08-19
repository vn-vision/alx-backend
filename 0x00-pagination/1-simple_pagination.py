#!/usr/bin/env python3
'''
index_range: takes two arguments page and page_size
    @page: page number
    @page_size: page size

Return: tuple of ize two containing start index and rend inde
'''

import csv
import math
from typing import Tuple, List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two integers page and page size with default value 10
        returns appropriate dataset
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        index = index_range(page, page_size)
        start_ind = index[0]
        end_ind = index[1]
        data = self.dataset()
        datasize = int(len(data))

        if start_ind > datasize:
            return []
        if end_ind > datasize:
            return data[start_ind:]

        return data[start_ind:end_ind]
