def valid_parentheses(string):
    if string.count('(') == string.count(')'):
        parentheses = [x for x in string if not x.isalpha()]
        string = ''.join(parentheses)
        while '()' in string:
            parentheses = list(string.partition('()'))
            parentheses.remove(parentheses[1])
            string = ''.join(parentheses)
        return not string
    return False
