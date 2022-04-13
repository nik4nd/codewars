def rgb(r, g, b):
    rgb = [r, g, b]
    for i in range(len(rgb)):
        if rgb[i] < 0:
            rgb[i] = 0
        elif rgb[i] > 255:
            rgb[i] = 255
        rgb[i] = hex(rgb[i])[2:].upper()
        if len(rgb[i]) < 2:
            rgb[i] = '0' + rgb[i]
    return ''.join(rgb)
