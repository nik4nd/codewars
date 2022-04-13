def dirReduc(arr):
    result = []
    nswe = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    for i in arr:
        result.pop() if result and nswe[i] == result[-1] else result.append(i)
    return result
