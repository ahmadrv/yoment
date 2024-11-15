from typing import List

def find_first(val: int, array: List[int], size: int) -> int:
    for i in range(size):
        if array[i] == val:
            return i
    return -1
