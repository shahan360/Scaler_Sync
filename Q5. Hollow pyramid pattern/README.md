Problem Name: Q5. Hollow pyramid pattern

Q5. Hollow pyramid pattern
Solved
Problem Description
Take an integer N as input, print the corresponding pattern for N.
For example if N = 5 then pattern will be like:
********** // 0 spaces
****__**** // 2 spaces
***____*** // 4 spaces
**______** // 6 spaces
*________* // 8 spaces
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
**** // 0 spaces
*__* // 2 spaces
Output 2:
****** // 0 spaces
**__** // 2 spaces
*____* // 4 spaces
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
15
16
17
18
19
20
21
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N):
        for j in range(2*N):
            # Print stars on the left side
            if j < N - i:
                print("*", end="")
            # Print spaces in the middle
            elif j < N - i + 2 * i:
                print(" ", end="")
            # Print stars on the right side
            else:
                print("*", end="")                 
        print("")  # Move to the next line after each row
    return 0
if __name__ == '__main__':
    main()
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
Running Test Cases...
> TestCase - Easy Success
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