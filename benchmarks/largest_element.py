from typing import List

def largest_element(arr: List[int], num: int) -> int:
    max_element = arr[0]
    for i in range(1, num):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element
