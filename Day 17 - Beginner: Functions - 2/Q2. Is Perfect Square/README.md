Problem Name: Q2. Is Perfect Square ?

Q2. Is Perfect Square ?
Solved
Problem Description
You are given a function that takes an integer argument A. Return 1 if A is a perfect square otherwise return 0.
A perfect square is an integer that is the square of an integer. For example 16 is perfect square as it is the square of an integer 4 (42 = 16)
Problem Constraints
1 <= A <= 108
Input Format
First argument is an integer A.
Output Format
Return an integer (0 or 1) based upon the question.
Example Input
Input 1:
A = 4
Input 2:
A = 1001
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Explanation 1:
sqrt(4) = 2
Explanation 2:
1001 is not a perfect square.
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Run
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
else:
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 16 - Beginner: Functions - 1
Day 18 - Beginner: Contest 2
Home
Upgrade to MS in Computer Science
Join Referral Program
2X Rewards
Earn
12000
₹25,000
on your 1st Referral
Refer and Earn
LEARN AND PRACTICE
All modules, classes and certifications
All career related classes and 1-1 mentor sessions
PLACEMENT
Earn skill certificate to unlock job opportunities
COMMUNITY
ACTION CENTRE
New
MORE
Day 17 - Beginner: Functions - 2
Mandatory
0
100%
Class Attendance
17 / 17
Problems Solved
100%
New
All
Q 1
Q 2
Q 3
Q 4
Q 5
Q 6
Q 7
Question
Your Score: 200
Max Score:
200

## Problem Constraints

1 <= A <= 108

## Input Format

First argument is an integer A.

## Output Format

Return an integer (0 or 1) based upon the question.

## Solution

See `Solution.py` for the implementation.