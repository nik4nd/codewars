def get_count(sentence):
    return sum([sentence.count(x) for x in ['a', 'e', 'i', 'o', 'u']])
