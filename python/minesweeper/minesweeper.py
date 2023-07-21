def annotate(minefield):
    if minefield == []:
        return minefield
    key = [list(row) for row in minefield]
    width = len(key[0])
    for i in range(0, len(key)):
        if len(key[i]) != width:
            raise ValueError('Minefield is not a consistent width.')
        for j in range(0, width):
            if key[i][j] == '*':
                continue
            elif key[i][j] == ' ':
                key[i][j] = get_mine_count(i,j,minefield)
            else:
                raise ValueError('Minefield contains invalid characters.')
    key = [''.join(row) for row in key]
    return key

def get_mine_count(row,col,minefield):
    mines = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            x = row + i
            y = col + j
            if x < 0 or y < 0:
                continue
            try:
                if minefield[x][y] == '*':
                    mines += 1
            except IndexError:
                pass
    if mines > 0:
        return str(mines)
    else:
        return ' '