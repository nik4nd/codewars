def max_sequence(arr):
    if len(arr) > 0:
        if max(arr) < 0:
            return 0
        maximum = arr[0]
        current = 0
        for i in arr:
            if current < 0:
                current = 0
            current += i
            maximum = max(maximum, current)
        return maximum
    return 0
