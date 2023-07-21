NUMERALS = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

PRECEDERS = {1, 10, 100}

def roman(number):
    roman = []

    for i in reversed(list(NUMERALS.keys())):
        while number >= i:
            roman.append(NUMERALS[i])
            number -= i
        try:
            pre = ({i//5, i//10} & PRECEDERS).pop()
        except KeyError:
            continue
        if number >= i - pre:
            roman.append(NUMERALS[pre] + NUMERALS[i])
            number -= i - pre
    return ''.join(roman)


