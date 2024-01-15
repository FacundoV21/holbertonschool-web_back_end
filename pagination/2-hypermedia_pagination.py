#!/usr/bin/env python3
"""
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """returns the index and page"""
    fPage = (page - 1) * page_size
    return (fPage, fPage + page_size)


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
        """ gets the index of a page"""
        assert (type(page), type(page_size)) == (int, int)
        assert page > 0
        assert page_size > 0

        data = self.dataset()
        index = index_range(page, page_size)

        if len(data) > index[1]:
            return data[index[0]:index[1]]

        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Function to get the right pagination"""

        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": None if len(data) == 0 else page + 1,
            "prev_page": None if page < 2 else page - 1,
            "total_pages": math.ceil(len(self.dataset()) / page_size),
        }
