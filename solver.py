# Sudoku Solver -

# This python file will provide executable python code that will solve sudoku
# puzzles using a backtracking algorithm. See the readme for more information.


board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

# Accepts a board and a spot on the board (denoted by row and column) and checks
# if putting that value on that spot of the board is valid
def isValid(board, row, col, value):
    # Checks whether the inserted number would invalidate the column or row
    for x in range(0,9):
        if board[row][x] == value and x != col:
            return False;
        if board[x][col] == value and x != row:
            return False;
    # Checks for whether the inserted number would invalidate the 3x3 box
    for r in range((row//3) * 3, (row//3) * 3 + 3):
        for c in range((col//3) * 3, (col//3) * 3 + 3):
            if board[r][c] == value and r != row and c != col:
                return False;
    return True;

# Finds the next empty square for where values can be guessed
def nextSquare(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return row, col
    return -1, -1

# Prints out the board in a more readable fashion
def printBoard(board):
    for x in board:
        print(x)
    return

# Actually solves the puzzle recursively
def solve(board):
    row, col = nextSquare(board)
    if row == -1:
        return True
    for x in range(1,10):
        if isValid(board, row, col, x):
            board[row][col] = x;
            if solve(board) == False:
                board[row][col] = 0
            else:
                printBoard(board)
                print()
    return False


# Code to run the sudoku puzzle by just running it
print("Hi, welcome to the sudooku solver! Please enter your puzzle:")
for x in range(9):
    line = raw_input('Enter row #' + str(x+1) + ':   ')
    info = int(line)
    for y in range(8,-1,-1):
        board[x][y] = info % 10
        info /= 10
print()
print("Your board:")
print()
printBoard(board)
print()
print("Solution:")
solve(board)
