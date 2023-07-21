DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]

def spiral_matrix(size):
    matrix = [[None]*size for _ in range(size)]
    cell = (0,0)
    dir_index = 0
    for i in range(1, size**2 + 1):
        matrix[cell[0]][cell[1]] = i
        next_cell = tuple(a+b for a,b in zip(cell, DIRECTIONS[dir_index]))
        if (not (0 <= next_cell[0] < size and 0 <= next_cell[1] < size) or
            matrix[next_cell[0]][next_cell[1]] is not None):
            dir_index = (dir_index + 1) % len(DIRECTIONS)
            next_cell = tuple(a+b for a,b in zip(cell, DIRECTIONS[dir_index]))
        cell = next_cell
    return matrix




    


        
    
