"""
Using recursive functions on a large 2 dimensional grid, you implement flood filling algorithm and have to improve the performance of your code using memoization.

Algorithm: Flood Fill, Memoization (Dynamic Programming), BFS, recursion
Rule: Your program receives as input a list of coordinates. For each one you must determine the surface area of the lake which is located there. If there is no lake, then the surface area equals 0.
Input:
Line 1: Two integers L and H representing the width and height of the map.
Next H lines: L characters representing one line of the ASCII map.
Next line: An integer N representing the number of coordinates to be processed.
Next N lines: Two integers X and Y representing the coordinates for which you have to compute the surface area of the lake.
Output:
N lines: The surface area of the lake for each coordinate.
"""
from functools import cache

def _(x,y):
    return y * l + x

@cache
def getLakeSurface(grid,x,y,ndx):
    stack = [(x,y)]
    surface = 0

    while stack:
        x,y = stack.pop()
        if grid[y][x] == 'O':
            grid = [list(row) for row in grid]
            grid[y][x] = ndx
            grid = [tuple(row) for row in grid]
            surface += 1
            if x > 0:
                stack.append((x-1,y))
            if x < l-1:
                stack.append((x+1,y))
            if y > 0:
                stack.append((x,y-1))
            if y < h-1:
                stack.append((x,y+1))
    return surface


l = int(input())
h = int(input())
grid = ()
for y in range(h):
    row = input()
    grid += tuple(row[x] for x in range(l)),
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    print(getLakeSurface(grid,x,y,i+2))
