def productFib(prod):
    fib = [0, 1]
    while fib[-1] * fib[-2] < prod:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] * fib[-2] == prod:
        return [fib[-2], fib[-1], True]
    else:
        return [fib[-2], fib[-1], False]
