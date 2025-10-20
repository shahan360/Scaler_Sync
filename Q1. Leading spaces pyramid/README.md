Problem Name: Q1. Leading spaces pyramid

Q1. Leading spaces pyramid
Solved
Problem Description
Take an integer N as input, print the corresponding pattern for N.
For example if N = 5 then pattern will be like:
____*
___**
__***
_****
*****
Note : Here '_' represents space for explanation purpose only. You have to print space in your code.
Problem Constraints
1 <= N <= 100
Input Format
First and only line of input contains a single integer N.
Output Format
Output the pattern corresponding to the given N.
Example Input
Input 1:
 2
Input 2:
 3
Example Output
Output 1:
 *
**
Output 2:
  *
 **
***
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
# write here
N = int(input())
for i in range(1,N+1):
    for k in range(N-i):
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

1 <= N <= 100

## Input Format

First and only line of input contains a single integer N.

## Output Format

Output the pattern corresponding to the given N.

## Solution

See `Solution.py` for the implementation.