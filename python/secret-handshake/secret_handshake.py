def commands(number):
    actions = [
        (1, 'wink'),
        (2, 'double blink'),
        (4, 'close your eyes'),
        (8, 'jump')
    ]

    array = [action[1] for action in actions if action[0] & number]
    if 16 & number:
        array.reverse()
    return array
