def anagrams(word, words):
    return [x for x in words if sorted(set(word)) == sorted(set(x)) and \
            len(word) == len(x)]
