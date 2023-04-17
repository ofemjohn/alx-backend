#!/usr/bin/env python3
'''
return in a list for those
particular pagination parameters.
'''
import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    '''return a turple '''
    start_index = (page - 1) * (page_size)
    ending_index = start_index + page_size
    return (start_index, ending_index)


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
        """ obtains the indexes and return corresponding pages """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        ''' returns a dictionary '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        to_pages = math.floor(len(self.dataset()) / page_size)
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < to_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': to_pages
                }
