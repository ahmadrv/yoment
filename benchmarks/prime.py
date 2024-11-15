def check_prime(n: int) -> int:
    for c in range(2, n):
        if n % c == 0:
            return 0
    return 1
