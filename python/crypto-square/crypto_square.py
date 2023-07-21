import math
import re

def cipher_text(plain_text):
    text = normalize(plain_text)
    cols = math.ceil(math.sqrt(len(text)))
    square = []
    i = 0
    while i < len(text):
        fragment = text[i:i+cols].ljust(cols, ' ')
        square.append(fragment)
        i += cols
    columns = []
    for i in range(0, cols):
        columns.append(column(square, i))
    return ' '.join(columns)

def normalize(text):
    return re.sub(r'[^A-Za-z0-9]', '', text).lower()

def column(square, col):
    text = []
    for row in square:
        text.append(row[col])
    return ''.join(text)

