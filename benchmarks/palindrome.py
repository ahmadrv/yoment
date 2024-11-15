def palindrome(num: int) -> bool:   # [ ]: Is it OK if type annotation of output be bool?
    reverse_num = 0
    temp = num

    while temp != 0:
        remainder = temp % 10
        reverse_num = reverse_num * 10 + remainder
        temp //= 10

    return reverse_num == num
