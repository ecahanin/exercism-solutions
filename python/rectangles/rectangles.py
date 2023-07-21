from itertools import combinations


def rectangles(strings):
    corners = []
    for i, row in enumerate(strings):
        for j, char in enumerate(row):
            if char == '+':
                corners.append((i,j))
    rectangles = []
    for nw in corners:
        nes = [(nw[0], nw[1] + 1 + i) for i, char in enumerate(strings[nw[0]][nw[1]+1:]) if char == '+']
        for ne in nes:
            sws = [(nw[0] + 1 + j, nw[1]) for j, char in enumerate(column(strings, nw[1])[nw[0]+1:]) if char == '+']
            for sw in sws:
                se = (sw[0],ne[1])
                if strings[se[0]][se[1]] == '+':
                    if has_sides([nw, ne, sw, se], strings):
                        rectangles.append([nw, ne, sw, se])
    return len(rectangles)
    
def column(strings, i):
    return ''.join([row[i] for row in strings])

def has_sides(corners, strings):
    nw, ne, sw, se = corners
    top = strings[nw[0]][nw[1]:ne[1]+1]
    bottom = strings[sw[0]][sw[1]:se[1]+1]
    left = column(strings, nw[1])[nw[0]:sw[0]+1]
    right = column(strings, ne[1])[ne[0]:se[0]+1]
    return (top.count('-') + top.count('+') == len(top) and
        bottom.count('-') + bottom.count('+') == len(bottom) and
        left.count('|') + left.count('+') == len(left) and
        right.count('|') + right.count('+') == len(right))







    
                    
                

    
        





