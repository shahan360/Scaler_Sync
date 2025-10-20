Problem Name: Q1. Factorial of N - Functions

Q1. Factorial of N - Functions
Solved
Problem Description
Given a number N, return factorial of N.
Required Information for factorial :
n! = n * (n-1) * (n-2) * . . . . . . * 3 * 2 * 1.
for eg. 5! = 5 * 4 * 3 * 2 * 1 = 120.
Corner Case :
0! = 1
Problem Constraints
0 <= N <= 10
Input Format
Argument A which is given number N.
Output Format
Return the answer from factorial function.
Example Input
Input 1 :
5
Input 2 :
6
Example Output
Output 1 :
120
Output 2 :
720
Example Explanation
Explanation 1 :
When N is 5, 5! is 5 * 4 * 3 * 2 * 1 which is 120.
Explanation 2 :
When N is 6, 6! is 6 * 5 * 4 * 3 * 2 * 1 which is 720.
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Run
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
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        fact = 1
        for i in range(1,A+1):
            fact = fact*i
        return fact    
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 15 - Beginner: Iterations - Patterns
Day 17 - Beginner: Functions - 2

## Problem Constraints

0 <= N <= 10

## Input Format

Argument A which is given number N.

## Output Format

Return the answer from factorial function.

## Example Input

Input 1 :
5

Input 2 :
6

## Solution

See `Solution.py` for the implementation.