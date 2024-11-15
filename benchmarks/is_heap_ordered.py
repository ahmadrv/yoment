from typing import List

def is_heap_ordered(a: List[int], n: int) -> int:
    for i in range((n - 2) // 2 + 1):
        if a[i] >= a[2 * i + 1] or a[i] >= a[2 * i + 2]:
            return 0
    return 1
