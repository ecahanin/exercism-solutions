LINES = [
    ('house that Jack built', ''),
    ('malt', 'lay in'),
    ('rat', 'ate'),
    ('cat', 'killed'),
    ('dog', 'worried'),
    ('cow with the crumpled horn', 'tossed'),
    ('maiden all forlorn', 'milked'),
    ('man all tattered and torn', 'kissed'),
    ('priest all shaven and shorn', 'married'),
    ('rooster that crowed in the morn', 'woke'),
    ('farmer sowing his corn', 'kept'),
    ('horse and the hound and the horn', 'belonged to')
]


def recite(start_verse, end_verse):
    output = [build_verse(start_verse)]
    if start_verse < end_verse:
        output.extend(recite(start_verse + 1, end_verse))
    return output

def build_verse(verse):
    output = "This is the "
    for line in LINES[verse-1::-1]:
        obj, verb = line
        output += obj
        if verb:
            output += f" that {verb} the "
    output += "."
    return output
