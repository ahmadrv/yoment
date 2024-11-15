from typing import List

def compare_arrays(x: List[int], y: List[int], size: int) -> int:
    for i in range(size):
        if x[i] < y[i]:
            return -1
        elif x[i] > y[i]:
            return 1
    return 0
