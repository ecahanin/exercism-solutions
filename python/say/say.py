numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

groups = [
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand')
]

def say(number):
    if number > 999999999999 or number < 0:
        raise ValueError('Number must be between 0 and 999,999,999,999.')
    output = ''
    for group in groups:
        if number >= group[0]:
            output += parse_hundreds(number//group[0]) + ' ' + group[1] + ' '
            number -= (number//group[0])*group[0]
    if output == '' or number:
        output += parse_hundreds(number)
    return output.strip()

def parse_hundreds(part):
    hundreds = part // 100
    tens = part % 100
    if hundreds and tens:
        return f'{numbers[hundreds]} hundred {parse_tens(tens)}'
    elif hundreds:
        return f'{numbers[hundreds]} hundred'
    else:
        return parse_tens(tens)

def parse_tens(part):
    if part < 20:
        return numbers[part]
    elif part < 100:
        if part % 10 == 0:
            return numbers[part]
        else:
            return f'{numbers[part//10*10]}-{numbers[part%10]}'
