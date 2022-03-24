def unique_in_order(iterable):
    result = []
    if len(iterable) > 0:
        last = iterable[0]
        result.append(last)
        for i in range(1, len(iterable)):
            if iterable[i] != last:
                last = iterable[i]
                result.append(last)
    return result
