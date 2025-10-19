Problem Name: Q1. Count Factors - 2

Q1. Count Factors - 2
Solved
Problem Description
Given an integer A, you need to find the count of it's factors.
Factor of a number is the number which divides it perfectly leaving no remainder.
Example : 1, 2, 3, 6 are factors of 6
Problem Constraints
1 <= A <= 109
Input Format
First and only argument is an integer A.
Output Format
Return the count of factors of A.
Example Input
Input 1:
5
Input 2:
10
Example Output
Output 1:
2
Output 2:
4
Example Explanation
Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.
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
22
23
24
25
import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c = 0
        # k = len(A);
        #Brute Force Case
        # for i in range(1,A+1):
        #     if A%i==0:
        #         c+=1
        # return c 
        #optimization case
        for i in range(1, int(math.sqrt(A))+1):
            if A%i==0:
                if (i==A/i):
                    c+=1
                else:
                    c+=2
        return c                                         
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
Running Test Cases...
> TestCase - Easy Success
TestTest With Custom Input
Submit
Day 32 - Beginner Language Test: Discussion
Day 34 - DSA: Time Complexity - 1

## Problem Constraints

1 <= A <= 109

## Input Format

First and only argument is an integer A.

## Output Format

Return the count of factors of A.

## Solution

See `Solution.py` for the implementation.