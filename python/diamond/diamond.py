from string import ascii_uppercase as alphabet


def rows(letter):
    index = alphabet.find(letter)
    rows = build_line(index, range(index + 1))
    if index > 0:
        rows.extend(build_line(index, range(index - 1, -1, -1)))
    return rows


def build_line(index, index_range):
    rows = []
    for i in index_range:
        line = " " * (index - i) + alphabet[i] + " " * i
        line += line[-2::-1]
        rows.append(line)
    return rows
