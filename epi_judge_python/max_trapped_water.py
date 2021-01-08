from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    low, high = 0, len(heights)-1
    maxWater = 0

    while low < high:
        lowerHeight = min(heights[low], heights[high])
        maxWater = max(maxWater, lowerHeight * (high-low))

        if heights[low] < heights[high]:
            low += 1
        else:
            high -= 1

    return maxWater


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
