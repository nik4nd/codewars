def get_middle(s):
    if len(s) == 1 or len(s) == 2: return s
    even, odd = (len(s)-2)//2, (len(s)-1)//2
    return s[even:-even] if len(s) % 2 == 0 else s[odd:-odd]
