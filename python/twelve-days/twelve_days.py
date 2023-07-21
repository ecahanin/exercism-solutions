day_gifts = [
    ('first', 'a Partridge in a Pear Tree'),
    ('second', 'two Turtle Doves'),
    ('third', 'three French Hens'),
    ('fourth', 'four Calling Birds'),
    ('fifth', 'five Gold Rings'),
    ('sixth', 'six Geese-a-Laying'),
    ('seventh', 'seven Swans-a-Swimming'),
    ('eighth', 'eight Maids-a-Milking'),
    ('ninth', 'nine Ladies Dancing'),
    ('tenth', 'ten Lords-a-Leaping'),
    ('eleventh', 'eleven Pipers Piping'),
    ('twelfth', 'twelve Drummers Drumming'),
]

def recite(start_verse, end_verse):
    verses = []
    for n in range(start_verse, end_verse+1):
        verses.append(verse(n))
    return verses
    
def verse(verse):
    text = f'On the {day_gifts[verse-1][0]} day of Christmas my true love gave to me: '
    for n in range(verse-1, 0,-1):
        text += f'{day_gifts[n][1]}, '
    if verse != 1:
        text += 'and '
    text += f'{day_gifts[0][1]}.'
    return text