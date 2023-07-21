class Queen:
    def __init__(self, row, column):
        if 0 <= row <= 7 and 0 <= column <= 7:
            self.row = row
            self.column = column
        else:
            raise ValueError('invalid position')

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("queens can't be on the same space")
        elif self.row == another_queen.row or self.column == another_queen.column:
            return True
        elif abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        else:
            return False

