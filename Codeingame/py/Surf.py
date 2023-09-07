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
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = None
        self.visited = 0
        self.neighbours = []
    
    def pushVal(self, val):
        self.val = val
    
    def addNeighbour(self, node):
        self.neighbours.append(node)

class Surface:
    def __init__(self,l,h):
        self.l = l
        self.h = h
        self.grid = [[ _ for _ in range(h)] for _ in range(l)] # 2D array of characters representing the map
        self.gridOfNodes = [[ Node(i,j) for j in range(h)] for i in range(l)] # 2D array of nodes representing the map  

    def addNode(self, x, y, val):
        self.grid[x][y] = val
        self.gridOfNodes[x][y].pushVal(val)

    def addNeighbours(self):
        for i in range(self.l):
            for j in range(self.h):
                # add all neighbours
                if i > 0:
                    self.gridOfNodes[i][j].addNeighbour(self.gridOfNodes[i-1][j])
                if i < self.l-1:
                    self.gridOfNodes[i][j].addNeighbour(self.gridOfNodes[i+1][j])
                if j > 0:
                    self.gridOfNodes[i][j].addNeighbour(self.gridOfNodes[i][j-1])
                if j < self.h-1:
                    self.gridOfNodes[i][j].addNeighbour(self.gridOfNodes[i][j+1])
                # print(f'({i},{j})')
                # for neighbour in self.gridOfNodes[i][j].neighbours:
                #     print(f'({i},{j}) -> ({neighbour.x},{neighbour.y}): {neighbour.val}')

    def resetVisited(self):
        for i in range(self.l):
            for j in range(self.h):
                self.gridOfNodes[i][j].visited = 0
    
    # Flood Fill Algorithm, recursive and memoization (Dynamic Programming)
    @cache
    def floodFill(self, x, y):
        if self.gridOfNodes[x][y].visited == 1:
            return 0
        else:
            self.gridOfNodes[x][y].visited = 1
            if self.gridOfNodes[x][y].val == 'O':
                return 1 + sum([self.floodFill(neighbour.x, neighbour.y) for neighbour in self.gridOfNodes[x][y].neighbours])
            else:
                return 0
    # Optimize the algorithm
    @cache
    def OptimizeAlgo(self, x, y, ndx):
        # Stack
        stack = [self.gridOfNodes[x][y]]
        cnt = 0

        while len(stack) > 0:
            node = stack.pop()
            if node.visited == 0:
                node.visited = 1
                if node.val == 'O':
                    cnt += 1
                    for neighbour in node.neighbours:
                        stack.append(neighbour)
        return cnt



if __name__ == "__main__":
    l = int(input())
    h = int(input())
    wrap = []
    surface = Surface(l,h)
    for i in range(h):
        line = input()
        for j in range(l):
            surface.addNode(j,i,line[j])
    surface.addNeighbours()
    n = int(input()) # Number of coordinates 
    for i in range(n):
        (x,y) = [int(j) for j in input().split()]
        wrap.append((x,y))
    for _ in wrap:
        (x,y) = _
        surface.resetVisited()
        print(surface.OptimizeAlgo(x,y))