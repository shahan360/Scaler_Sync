Problem Name: Q6. Two Line Star Pattern

Q6. Two Line Star Pattern
Solved
Problem Description
Print a pattern consisting of N rows, where each row contains an asterisk (*) at the beginning and end of the line, with N-2 spaces in between.
The Pattern should look like:
*<N-2 Spaces>*
Print the above pattern for a total of N Rows.
Refer Example ouput, for better clarification.
Problem Constraints
2 <= N <= 100
Input Format
First and only line of input contains a single integer N.
Output Format
Output the pattern corresponding to the given N.
Example Input
Input 1:
 2
Input 2:
 4
Example Output
Output 1:
**
**
Output 2:
*  *
*  *
*  *
*  *
Example Explanation
Explanation 1:
 Here N = 2,  So each row should have N - 2 spaces which is 0.
 Thus the N rows(i.e, 2 rows) should be in the form (asterisk)(0 spaces)(asterisk)
Explanation 2:
 Here N = 4,  So each row should have N - 2 spaces which is 2.
 Thus the N rows(i.e, 4 rows) should be in the form (asterisk)(2 spaces)(asterisk)
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
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N):
        print("*", end='') # Print the first asterisk without a newline
        for j in range(N-2):
            print(" ",end='') # Print spaces without a newline
        print("*") # Print the last asterisk with a newline     
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

2 <= N <= 100

## Input Format

First and only line of input contains a single integer N.

## Output Format

Output the pattern corresponding to the given N.

## Solution

See `Solution.py` for the implementation.