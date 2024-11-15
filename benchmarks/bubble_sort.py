def bubble_sort(lst: list, n: int) -> None:
    for c in range(n - 1):
        for d in range(n - c - 1):
            if lst[d] > lst[d + 1]:
                t = lst[d]
                lst[d] = lst[d + 1]
                lst[d + 1] = t
