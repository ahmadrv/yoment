from typing import List

def LCIS(arr1: List[int], n: int, arr2: List[int], m: int) -> int:
    # table[j] is going to store length of LCIS ending with arr2[j]
    table = [0] * m

    # Traverse all elements of arr1[]
    for i in range(n):
        # Initialize current length of LCIS
        current = 0

        # For each element of arr1[], traverse all elements of arr2[]
        for j in range(m):
            # If both the arrays have the same elements
            if arr1[i] == arr2[j]:
                if current + 1 > table[j]:
                    table[j] = current + 1

            # Now seek for previous smaller common element for the current element of arr1
            if arr1[i] > arr2[j]:
                if table[j] > current:
                    current = table[j]

    # Find the maximum value in table[] as the result
    result = 0
    for i in range(m):
        if table[i] > result:
            result = table[i]

    return result
