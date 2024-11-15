def insertion_sort(lst: list, count: int) -> int:
    for i in range(1, count):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp

    return 0
