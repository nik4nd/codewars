def solution(s):
    search_start, beginning = 0, 0
    words = []
    for char in s:
        if char.isupper():
            ending = s.index(char, search_start)
            words.append(s[beginning:ending])
            beginning = ending
            search_start = beginning + 1
    words.append(s[beginning:])
    return ' '.join(words)
