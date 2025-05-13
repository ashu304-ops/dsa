def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)  # Horizontal separator every 3 rows

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")  # Vertical separator every 3 columns

            value = board[row][col]
            if value != 0:
                print(value, end=" ")
            else:
                print(".", end=" ")
        print()

def find_empty_spot(board):
    for row  in range(9):
        for  col  in range(9):
            if board[row][col]==0:
                return  row,col
    return  None

def isvalid(board,number,position):
    row,col=position
#check row
    if  number  in board[row]:
        return False
# check  columns    
    for  i in  range(9):
        if  board[i][col]==number:
            return False
#check 3*3 box
    box_row= (row//3)*3
    box_column= (col//3)*3
    for i in range(3):
        for j  in range(3):
            if board[box_row+i][box_column+j]==number:
                return  False
    return True

# important  part backtracking
def solve(board):
    empty = find_empty_spot(board)
    if not empty:
        return True  # Puzzle is solved!

    row, col = empty

    for number in range(1, 10):  # Try numbers 1–9
        if isvalid(board, number, (row, col)):
            board[row][col] = number  # Try it

            if solve(board):  # Recursively solve rest
                return True

            board[row][col] = 0  # Backtrack if needed

    return False  


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(print_board(board))
            
            