"""
A sudoku grid consists of 9×9 = 81 cells split in 9 sub-grids of 3×3 = 9 cells.
For the grid to be correct, each row must contain one occurrence of each digit (1 to 9), each column must contain one occurrence of each digit (1 to 9) and each sub-grid must contain one occurrence of each digit (1 to 9).

You shall answer true if the grid is correct or false if it is not.
Input
9 rows of 9 space-separated digits representing the sudoku grid.
Output
true or false
Constraints
For each digit n in the grid: 1 ≤ n ≤ 9.
"""
if __name__ == '__main__':
    broad = []  
 
    for i in range(9):
        broad.append(list(map(int, input().split())))
    # check row
    for row in broad:
        if len(set(row)) != 9:
            print('false')
            exit()
    
    # check column
    for i in range(9):
        col = []
        for j in range(9):
            col.append(broad[j][i])
        if len(set(col)) != 9:
            print('false')
            exit()
    
    # check sub-grid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub = []
            for k in range(3):
                for l in range(3):
                    sub.append(broad[i+k][j+l])
            if len(set(sub)) != 9:
                print('false')
                exit()
    
    print('true')