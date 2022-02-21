def alphabet_position(text):
    alphabet = {}
    chars = [chr(x) for x in range(97, 123)]
    for i in range(len(chars)):
        alphabet[chars[i]] = str(i+1)
    return ' '.join([alphabet[x] for x in text.lower() if x in alphabet])
