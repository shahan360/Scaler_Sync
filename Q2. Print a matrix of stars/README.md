Problem Name: Q2. Print a matrix of stars

Q2. Print a matrix of stars
Solved
Problem Description
Given two integers N and M as inputs, print a rectangle of N * M stars.
For example if N = 3, M = 4 then pattern will be like:
****
****
****
Problem Constraints
2 <= N, M <= 100
Input Format
First line of input contains an integers N (no of rows).
Second line of input contains an integer M (no of cols).
Output Format
Output N * M rectangle of stars.
Example Input
Input 1:
 2
 3
Input 2:
 3
 1
Example Output
Output 1:
***
***
Output 2:
*
*
*
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
# write here
N = int(input())
M = int(input())
for i in range(N):
    for j in range(M):
        print("*", end="")
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

2 <= N, M <= 100

## Input Format

First line of input contains an integers N (no of rows).

Second line of input contains an integer M (no of cols).

## Output Format

Output N * M rectangle of stars.

## Solution

See `Solution.py` for the implementation.