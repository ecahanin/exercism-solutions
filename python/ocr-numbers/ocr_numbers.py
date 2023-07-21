DIGITS = {
    1: ("   ", "  |", "  |"),
    0: (" _ ", "| |", "|_|"),
    2: (" _ ", " _|", "|_ "),
    3: (" _ ", " _|", " _|"),
    4: ("   ", "|_|", "  |"),
    5: (" _ ", "|_ ", " _|"),
    6: (" _ ", "|_ ", "|_|"),
    7: (" _ ", "  |", "  |"),
    8: (" _ ", "|_|", "|_|"),
    9: (" _ ", "|_|", " _|")
}

DIGIT_LOOKUP = { value: key for key, value in DIGITS.items() }

def convert(input_grid):
    if len(input_grid) % 4 != 0 or len(input_grid[0]) % 3 != 0:
        raise ValueError('Input must be 4 lines per row of characters, with 3 columns per character')
    rows = [input_grid[i:i+4] for i in range(0,len(input_grid), 4)]
    result_string = ','.join([convert_row(row) for row in rows])
    return result_string
    

def convert_row(row):
    series = []
    for i in range(0, len(row[0]), 3):
        digit = tuple([row[i:i+3] for row in row[0:3]])
        series.append(digit)
    row_string = ''.join([str(DIGIT_LOOKUP.get(digit, '?')) for digit in series])
    return row_string



    
