def accum(s):
    letters = [s[i]*(i+1) for i in range(len(s))]
    return '-'.join([x.capitalize() for x in letters])
