def disemvowel(string_):
    return ''.join(['' if x in list('aeiouAEIOU') else x for x in string_])
