Problem Name: Q6. Hollow inverted pyramid pattern

Q6. Hollow inverted pyramid pattern
Solved
Problem Description
Take an integer N as input, print the corresponding pattern for N.
For example if N = 5 then pattern will be like:
*________* // 8 spaces
**______** // 6 spaces
***____*** // 4 spaces
****__**** // 2 spaces
********** // 0 spaces
NOTE: Here '_' is used to represent spaces. You have to print spaces in your code.
Problem Constraints
2 <= N <= 100
Input Format
First and only line of input contains a single integer N.
Output Format
Output the Full Pyramid pattern corresponding to the given N.
Example Input
Input 1:
 2
Input 2:
 3
Example Output
Output 1:
*__* // 2 spaces
**** // 0 spaces
Output 2:
*____* // 4 spaces
**__** // 2 spaces
****** // 0 spaces
NOTE: Here '_' is used to represent spaces. You have to print spaces in your code.
Example Explanation
 Print the pattern as described.
Python 3 (Python-3.8)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
# write here
N = int(input())
for i in range(1,N+1):
    for k in range(i):
        print("*",end="")
    for p in range(1,2*(N-i)+1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("")
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 14 - Beginner: Iterations : Loop - 3
Day 16 - Beginner: Functions - 1

## Problem Constraints

2 <= N <= 100

## Input Format

First and only line of input contains a single integer N.

## Output Format

Output the Full Pyramid pattern corresponding to the given N.

## Solution

See `Solution.py` for the implementation.