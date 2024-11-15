from typing import List

def equal_arrays(x: List[int], y: List[int], size: int) -> bool:    # [ ]: Same as others.
    for i in range(size):
        if x[i] != y[i]:
            return False
    return True
