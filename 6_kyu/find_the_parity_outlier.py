def find_outlier(integers):
    even, odd = [], []
    for i in sorted(integers):
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
        if len(even) > 1 and len(odd) != 0:
            return odd[0]
        elif len(odd) > 1 and len(even) != 0:
            return even[0]
