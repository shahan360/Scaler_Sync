Problem Name: Q4. Inverted Numeric Pyramid

Q4. Inverted Numeric Pyramid
Solved
Problem Description
Take an integer N as input, print the corresponding Numeric Inverted Half Pyramid pattern for N.
For example if N = 4 then pattern will be like:
1 2 3 4
1 2 3
1 2
1
Problem Constraints
1 <= N <= 100
Input Format
First and only line of input contains a single integer N.
Output Format
Output the Numeric Inverted Half Pyramid pattern corresponding to the given N.
NOTE: There should be no extra spaces after last integer and before first integer in any . All integers in any row in the pattern are separated by a single space.
Example Input
Input 1:
 2
Input 2:
 3
Example Output
Output 1:
1 2
1
Output 2:
1 2 3
1 2
1
Example Explanation
 Example Input 1
 We have the input of integer as 2. So there will be 2 rows. 
 The first row will have 2 integers separated by a single space (1 2)
 The next row will have 2-1 = 1 integer (1)
 As we do not have any more integers left we stop printing the pattern.
 Example Input 2
 We have the input of integer as 3. So there will be 3 rows. 
 The first row will have 3 integers separated by a single space (1 2 3)
 The next row will have 3-1 = 2 integers separated by a single space (1 2)
 The next row will have 2-1 = 1 integer.(1)
 As we do not have any more integers left we stop printing the pattern.
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
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N,0,-1):
        print(" ".join(str(j) for j in range(1, i+1))) 
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

Output the Numeric Inverted Half Pyramid pattern corresponding to the given N.

NOTE: There should be no extra spaces after last integer and before first integer in any . All integers in any row in the pattern are separated by a single space.

## Solution

See `Solution.py` for the implementation.