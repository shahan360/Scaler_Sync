Problem Name: Q3. Square root of a number

Q3. Square root of a number
Solved
Problem Description
Given a number A. Return square root of the number if it is perfect square otherwise return -1.
Note: A number is a perfect square if its square root is an integer.
Problem Constraints
1 <= A <= 108
Input Format
First and the only argument is an integer A.
Output Format
Return an integer which is the square root of A if A is perfect square otherwise return -1.
Example Input
Input 1:
A = 4
Input 2:
A = 1001
Example Output
Output 1:
2
Output 2:
-1
Example Explanation
Explanation 1:
sqrt(4) = 2
Explanation 2:
1001 is not a perfect square.
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
11
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sqrt = A**(1/2)
        sqrt2 = int(sqrt)
        if (sqrt2**2)==A:
            return sqrt2
        else:
            return -1
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 16 - Beginner: Functions - 1
Day 18 - Beginner: Contest 2

## Problem Constraints

1 <= A <= 108

## Input Format

First and the only argument is an integer A.

## Output Format

Return an integer which is the square root of A if A is perfect square otherwise return -1.

## Solution

See `Solution.py` for the implementation.