from typing import List

def binary_search(search: int, array: List[int], n: int) -> int:
    first = 0
    last = n - 1
    middle = (first + last) // 2

    while first <= last:
        if array[middle] < search:
            first = middle + 1
        elif array[middle] > search:
            last = middle - 1
        else:
            return middle
        middle = (first + last) // 2
    return -1
