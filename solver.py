# Sudoku Solver -

# This python file will provide executable python code that will solve sudoku
# puzzles using a backtracking algorithm. See the readme for more information.

# Accepts a board and a spot on the board (denoted by row and column) and checks
# if putting that value on that spot of the board is valid

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

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

def nextSquare(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return row, col
    return -1
