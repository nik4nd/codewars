from collections import Counter


def find_it(seq):
    return [k for k, v in Counter(seq).items() if v % 2 != 0][0]
