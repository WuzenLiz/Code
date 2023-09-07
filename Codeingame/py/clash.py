"""
Given an array array of integers of size n.
Our mission consists on printing the absolute value of the Max and Min difference between 2 successives indexes (i and i+1).
Input
Line 1 : An integer n that represent the size of the array.
Line 2 : An array of integers separated by space.
Output
Line 1 : Two integers min and max separated by a space.
Constraints
2 ≤ n ≤ 50
Example
Input
5
0 2 3 5 4
Output
1 2
"""
# Solution:
n = int(input())
arr = list(map(int, input().split()))

solver = lambda arr: [abs(arr[i] - arr[i+1]) for i in range(len(arr)-1)]
print(min(solver(arr)), max(solver(arr)))
