def dig_pow(n, p):
    numbers = [int(x) for x in list(str(n))]
    result = 0
    for i in numbers:
        result += i**p
        p += 1
    return result // n if result % n == 0 else -1
