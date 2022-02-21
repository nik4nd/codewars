def persistence(n):
    numbers = [n]
    while len(str(numbers[-1])) > 1:
        temp = 1
        for i in str(numbers[-1]):
            temp *= int(i)
        numbers.append(temp)
    return len(numbers) - 1
