def decode_morse(string):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', 'SOS': '...---...', '.': '.-.-.-', '!': '-.-.--'}
    symbols = []
    words = string.split('   ')
    for chars in words:
        for char in chars.split():
            for k, v in morse_code.items():
                if char == v:
                    symbols.append(k)
        symbols.append(' ')
    return ''.join(symbols).strip()
