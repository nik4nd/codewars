import re


def increment_string(strng):
    numbers = re.findall('[0-9]+', strng)
    if len(numbers) != 0:
        n = int(numbers[-1]) + 1
        if len(str(n)) < len(numbers[-1]):
            n = '0' * (len(numbers[-1]) - len(str(n))) + str(n)
        return f'{strng[:-len(numbers[-1])]}{n}'
    return f'{strng}{1}'
