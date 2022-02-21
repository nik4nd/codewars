def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(signature[-3] + signature[-2] + signature[-1])
    if len(signature) > n:
        return signature[:n]
    return signature
