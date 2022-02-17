from math import sqrt


def find_next_square(sq):
    if sqrt(sq).is_integer():
        return int(sqrt(sq) + 1)**2
    return -1
