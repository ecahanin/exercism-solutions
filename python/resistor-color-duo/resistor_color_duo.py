band_colors = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9',
}

def value(colors, limit=2):
    number = ''
    for color in colors[:limit]:
        number += band_colors[color]
    return int(number)



