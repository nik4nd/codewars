def create_phone_number(n):
    n = ''.join([str(x) for x in n])
    return f'({n[:3]}) {n[3:6]}-{n[6:]}'
