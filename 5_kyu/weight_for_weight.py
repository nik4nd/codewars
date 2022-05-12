def weight(number):
    return sum(int(x) for x in number)


def order_weight(strng):
    values = sorted(sorted(strng.split()), key=weight)
    return ' '.join(values)
