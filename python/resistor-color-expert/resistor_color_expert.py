BANDS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
TOLERANCE = {
    'grey': '±0.05%',
    'violet': '±0.1%',
    'blue': '±0.25%',
    'green': '±0.5%',
    'brown': '±1%',
    'red': '±2%',
    'gold': '±5%',
    'silver': '±10%',
}



def resistor_label(colors):
    if len(colors) == 1:
        ohms = BANDS[colors[0]]
        return prefix(ohms)
    if len(colors) == 4:
        ohms = (BANDS[colors[0]]*10 + BANDS[colors[1]]) * 10**(BANDS[colors[2]])
        return f'{prefix(ohms)} {TOLERANCE[colors[3]]}'
    if len(colors) == 5:
        ohms = (BANDS[colors[0]]*100 + BANDS[colors[1]]*10 + BANDS[colors[2]]) * 10**(BANDS[colors[3]])
        return f'{prefix(ohms)} {TOLERANCE[colors[4]]}'

def prefix(value):
    if value >= 1_000_000:
        return f"{f'{value/1_000_000}'.rstrip('0').rstrip('.')} megaohms"
    elif value >= 1_000:
        return f"{f'{value/1_000}'.rstrip('0').rstrip('.')} kiloohms"
    else:
        return f'{value} ohms'


    
