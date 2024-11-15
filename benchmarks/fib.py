def fib(count: int) -> int:
    first_term = 0
    second_term = 1
    next_term = 0

    for i in range(1, count + 1):
        if i <= 0:
            next_term = i
        else:
            next_term = first_term + second_term
            first_term = second_term
            second_term = next_term

    return next_term
