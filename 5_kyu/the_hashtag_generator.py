def generate_hashtag(s):
    if s == '':
        return False
    s = '#' + ''.join([x.capitalize() for x in s.strip().split()])
    return False if len(s) > 140 else s
