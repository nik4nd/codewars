def order(sentence):
    order = {}
    numbers = [str(x) for x in list(range(1, len(sentence.split()) + 1))]
    for i in sentence.split():
        for j in numbers:
            if j in i:
                order[j] = i
    return ' '.join([order[x] for x in numbers])
