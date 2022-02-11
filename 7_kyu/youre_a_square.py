from math import sqrt


def is_square(n):
    try:
        return sqrt(n).is_integer()
    except:
        return False
