from typing import List

def is_sorted(array: List[int], size: int) -> bool:     # [ ]: Same as `palindrome.py`. Is it Ok?
    for i in range(size - 1):
        if array[i] > array[i + 1]:
            return False
    return True
