from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    
    left, right = 0, len(A) - 1

    while left <= right:
        middle = left + (right-left) // 2
        if A[middle] == k:
            while middle > 0 and A[middle-1] == k:
                middle -= 1
            return middle
        elif A[middle] < k:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
