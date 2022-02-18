def digital_root(n):
    while n > 9:
        n = sum([int(x) for x in list(str(n))])
    return n
