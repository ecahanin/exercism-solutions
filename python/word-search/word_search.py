DIRECTIONS = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0, -1),
    (1, -1)
]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        startpoints = []
        #each startpoint is occurrence of first letter
        for i, row in enumerate(self.puzzle):
            for j in range(len(row)):
                if self.puzzle[i][j] == word[0]:
                    startpoints.append(Point(j, i))
        for point in startpoints:
            #for each startpoint, try each direction
            for dir in DIRECTIONS:
                slice = word[0]
                k = 1
                #for each direction, continue until it doesn't match the word
                while word[0:k] == slice:
                    (x, y) = dir
                    nextx = point.x + k * x
                    nexty = point.y + k * y
                    if self.in_grid(nextx, nexty):
                        slice += self.puzzle[nexty][nextx]
                        if slice == word:
                            return point, Point(nextx, nexty)
                        k += 1
                    else:
                        break
        return None
    
    def in_grid(self, x, y):
        return (0 <= x < len(self.puzzle[0])) and (0 <= y <len(self.puzzle))
