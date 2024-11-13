def greatest_of_3(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > z) and (y > x):
        return y
    else:
        return z
