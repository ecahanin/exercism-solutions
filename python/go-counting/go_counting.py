WHITE = 'W'
BLACK = 'B'
NONE = ' '


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board)

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        def get_neighbors():
            neighbors = set()
            for cell in territory:
                cell_neighbors = [
                    (cell[0] + 1, cell[1]),
                    (cell[0] - 1, cell[1]),
                    (cell[0], cell[1] + 1),
                    (cell[0], cell[1] - 1)
                ]
                [neighbors.add(cell) for cell in cell_neighbors \
                     if 0 <= cell[0] < self.width() and 0 <= cell[1] < self.height()]
            return neighbors
    
        def process_cell(cell):
            stone = self.board[cell[1]][cell[0]]
            if stone == ' ':
                territory.add(cell)
            else:
                stones.add(stone)

        if not( 0 <= x < self.width() and 0 <= y < self.height() ):
            raise ValueError('invalid - coordinate outside board')

        territory = set()
        stones = set(NONE)
        owner = NONE

        if self.board[y][x] != ' ':
            return owner, territory
        else:
            territory.add((x, y))
        while True:
            old_size = len(territory)
            neighbors = get_neighbors()
            list(map(process_cell, neighbors))
            if old_size == len(territory):
                break
        if len(stones) == 2:
            stones.remove(NONE)
            owner = stones.pop()
        return (owner, territory)
    
    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories = {
            'W': set(),
            'B': set(),
            ' ': set()
        }

        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == ' ':
                    stone, territory = self.territory(j, i)
                    territories[stone] = territories[stone] | territory

        return territories