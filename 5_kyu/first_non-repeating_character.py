def first_non_repeating_letter(string):
    for i in string:
        if string.count(i) == 1 and string.upper().count(i.upper()) == 1:
            return i
    return ''
