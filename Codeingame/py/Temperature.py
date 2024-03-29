"""
GOAL
Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
Game Input
Your program must read the data from the standard input and write the result on the standard output.
Input
Line 1: N, the number of temperatures to analyze

Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
"""

# Solution:

n = int(input())  # the number of temperatures to analyse
temps = [int(i) for i in input().split()]  # the N temperatures expressed as integers ranging from -273 to 5526

if n == 0:
    print(0)
else:
    # find closest to 0
    closest = temps[0]
    for i in range(1, n):
        if abs(temps[i]) < abs(closest):
            closest = temps[i]
        elif abs(temps[i]) == abs(closest):
            closest = max(closest, temps[i])
    print(closest)