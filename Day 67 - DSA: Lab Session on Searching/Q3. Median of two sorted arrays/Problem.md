Problem Name: Q3. Median of two sorted arrays

## Problem Description

Given two sorted arrays A and B of size M and N respectively, return the median of the two sorted arrays.
Round of the value to the floor integer [2.6=2, 2.2=2]

## Problem Constraints

0 <= M <= 105
0 <= N <= 105
-109 <= A[i], B[i] <= 109

## Input Format

First argument A is an array of integers.
First argument B is an array of integers.

## Output Format

## Example Input

Input 1:
A = [5, 7]
B = [6]
Input 2:
A = [1, 2]
B = [3, 4]

## Example Output

Output 1:
6
Output 2:
2

Example Explanation

Example 1:
merged array = [5, 6, 7] and median is 6.
Example 2:
merged array = [1, 2, 3, 4] and median is
(2 + 3) / 2 = 2.5
= floor(2.5)
= 2

## Example Explanation

Example 1:
merged array = [5, 6, 7] and median is 6.
Example 2:
merged array = [1, 2, 3, 4] and median is
(2 + 3) / 2 = 2.5
= floor(2.5)
= 2

## Solution

See `Solution.py` for the implementation.