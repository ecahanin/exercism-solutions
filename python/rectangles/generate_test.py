from random import choice

def generate_strings():
    chars = ['+', ' ', '-', '|']
    strings = []
    for x in range(100):
        row = []
        for _ in range(100):
            row.append(choice(chars))
        strings.append(''.join(row))
    return strings
