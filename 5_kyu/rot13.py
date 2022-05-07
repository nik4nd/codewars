import string


def rot13(message):
    result = []
    alphabet = string.ascii_lowercase[:]
    for i in message:
        if i.isalpha():
            letter = alphabet[(alphabet.index(i.lower()) + 13) % 26]
            if i.islower():
                result.append(letter)
            else:
                result.append(letter.upper())
        else:
            result.append(i)
    return ''.join(result)
