import re
from string import ascii_lowercase as alphabet, digits

def encode(plain_text, a, b):
    def encode_char(char):
        if char in digits:
            return char
        else:
            return alphabet[(a * alphabet.index(char) + b) % 26]

    def add_spaces(text):
        spaced = ''
        for i in range(0, len(text), 5):
            spaced += text[i:i+5] + ' '
        return spaced.strip()

    if is_coprime(a) == False:
        raise ValueError('a must be coprime with 26')
    text = re.sub(r'[^0-9a-z]', '', plain_text.lower())
    encoded = ''.join([encode_char(char) for char in text])
    return add_spaces(encoded)

def decode(ciphered_text, a, b):
    def decode_char(char):
        if char in digits:
            return char
        else:
            return alphabet[((alphabet.index(char) - b) * mmi_of_a) % 26]

    def mmi(a):
        for b in range(26):
            if (a * b) % 26 == 1:
                return b

    if is_coprime(a) == False:
        raise ValueError('a must be coprime with 26')
    text = ciphered_text.replace(' ', '')
    mmi_of_a = mmi(a)
    decoded = ''.join([decode_char(char) for char in text])
    return decoded

def is_coprime(a):
    for x in range(2, 27):
        if a % x == 0 and 26 % x == 0:
            return False
    return True