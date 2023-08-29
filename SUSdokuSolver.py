""" 
BACKTRACKING ALGORITHM
empty cell = "0"
"""

# Check if the board is valid
def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == str(num):
            return False
    # Check if the number is already in the column
    for j in range(9):
        if board[j][col] == str(num):
            return False
    # Check if the number is already in the 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == str(num):
                return False
    return True

def solve(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == "0":
                # Try all numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = str(num)
                        solve(board)
                        board[row][col] = "0"
                return
    # Print the solution
    for row in board:
        print("".join(row))
   
if __name__ == "__main__":
    broad = [input() for _ in range(9)]
    broad = [list(row) for row in broad]
    solve(broad)

