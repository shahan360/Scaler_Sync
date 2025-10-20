Problem Name: Q4. Inverted Half Pyramid

Q4. Inverted Half Pyramid
Solved
Problem Description
Given an integer N, print the corresponding Inverted Half Pyramid pattern for N.
For example if N = 4 then pattern will be like:
****
***
**
*
Problem Constraints
1 <= N <= 100
Input Format
First and only line of input contains a single integer N.
Output Format
Output the Inverted Half Pyramid pattern corresponding to the given N.
Example Input
Input 1:
 2
Input 2:
 3
Example Output
Output 1:
 **
 *
Output 2:
 ***
 **
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
8
9
10
11
12
13
14
15
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(1, N+1):
        for j in range(1,N+2-i):
            print("*",end="")
        print("")
    return 0
if __name__ == '__main__':
    main()
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

Output the Inverted Half Pyramid pattern corresponding to the given N.

## Solution

See `Solution.py` for the implementation.