
class ConnectGame:
    def __init__(self, board):
        board = board.replace(' ', '').split("\n")
        self.board = [[Cell(x, y, value) for x, value in enumerate(row)] for y, row in enumerate(board)]
        self.width = len(self.board[0])
        self.height = len(self.board)
        
    def get_winner(self):
        if self.check_win('X'):
            return 'X'
        elif self.check_win('O'):
            return 'O'
        else:
            return ''

    def check_win(self, player):
        winners = set()
        new_winners = []
        if player == 'O':
            new_winners = [cell for cell in self.row(0) if cell.value == 'O']
        elif player == 'X':
            new_winners = [cell for cell in self.col(0) if cell.value == 'X']
        while new_winners:
            winners.update(new_winners)
            neighbors = set()
            for cell in new_winners:
                neighbors.update(self.get_neighbors(cell))
            new_winners = [cell for cell in neighbors if cell.value == player and cell not in winners]

        if player == 'O':
            winning_edge_cells = self.row(-1)
        elif player == 'X':
            winning_edge_cells = self.col(-1)
        for cell in winning_edge_cells:
            if cell in winners:
                return True
        return False

    def row(self, index):
        return [x for x in self.board[index]]

    def col(self, index):
        return [row[index] for row in self.board]

    def get_neighbors(self, cell):
        potential_neighbors = [(cell.x, cell.y -1), (cell.x + 1, cell.y-1), (cell.x - 1, cell.y), 
                                (cell.x + 1, cell.y),(cell.x - 1, cell.y + 1),(cell.x, cell.y + 1)]
        neighbors = [self.board[y][x] for (x,y) in potential_neighbors if self.is_valid_cell(x,y)]
        return neighbors

    def is_valid_cell(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value