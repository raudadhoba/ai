class QueenChessBoard:
    def __init__(self, size):
        # Initialize the chessboard with a specified size
        self.size = size
        # Track the columns where queens are placed
        self.columns = []

    def place_in_next_row(self, column):
        # Place a queen in the next row
        self.columns.append(column)

    def remove_in_current_row(self):
        # Remove the queen from the current row and return its column
        return self.columns.pop()

    def is_this_column_safe_in_next_row(self, column):
        # Determine the index of the next row
        row = len(self.columns)
        # Check if the column is already occupied
        if column in self.columns:
            return False
        # Check diagonals
        for queen_row, queen_column in enumerate(self.columns):
            # Check for diagonal conflicts
            if queen_column - queen_row == column - row or (self.size - queen_column) - queen_row == (self.size - column) - row:
                return False
        return True

    def display(self):
        # Display the current configuration of the board
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()

def solve_queen(size):
    """Display a chessboard for each possible configuration of placing n queens on an n x n chessboard and print the number of such configurations."""
    board = QueenChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0

    # Iterate over rows of the board
    while True:
        # Place a queen in the next row
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        # If could not find a column to place in or if the board is full
        if column == size or row == size:
            # If the board is full, we have a solution
            if row == size:
                board.display()
                print()
                number_of_solutions += 1
                # Backtrack by removing the last queen placed
                board.remove_in_current_row()
                row -= 1
            
            # Backtrack
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                # All queens removed, thus no more possible configurations
                break
            
            # Try previous row again
            row -= 1
            # Start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column

    print('Number of solutions:', number_of_solutions)

# Get user input and start solving the N-Queens problem
n = int(input('Enter n: '))
solve_queen(n)
