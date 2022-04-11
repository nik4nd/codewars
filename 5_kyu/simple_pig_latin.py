def pig_it(text):
    words = []
    for i in text.split():
        words.append(i[1:] + i[0] + 'ay') if i.isalpha() else words.append(i)
    return ' '.join(words)
