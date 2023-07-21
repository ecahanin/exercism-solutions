NUMBERS = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def recite(start, take=1):
    song = []
    for i in range(take):
        song.extend(stanza(start - i))
        if i < take - 1:
            song.append("")
    return song

def stanza(number):
    firstlines = f"{NUMBERS[number].capitalize()} green bottle{'s' if number != 1 else ''} hanging on the wall,"
    thirdline = "And if one green bottle should accidentally fall,"
    lastline = f"There'll be {NUMBERS[number-1]} green bottle{'s' if number-1 != 1 else ''} hanging on the wall."
    return [firstlines, firstlines, thirdline, lastline]
