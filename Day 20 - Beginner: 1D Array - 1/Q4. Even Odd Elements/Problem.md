Problem Name: Q4. Even Odd Elements

## Problem Description

You are given T(number of test cases) integer arrays. For each array A, you have to find the value of absolute difference between the counts of even and odd elements in the array.

## Problem Constraints

1 <= T <= 10

1 <= |A| <= 105

1 <= A[i] <= 109

## Input Format

First line contains a single integer T.

Each of the next T lines begin with an integer denoting the length of the array A (|A|), followed by |A| integers which indicate the elements in the array.

## Output Format

For each test case, print an integer in a separate line.

## Example Input

Input 1:
1
4 1 2 3 4
Input 2:
2
4 2 3 5 1
1 4

## Example Output

Output 1:
0
Output 2:
2
1

Example Explanation

## Example Explanation

Explanation 1:

For 1st test case:
The array is [1, 2, 3, 4].
Number of even elements = 2
Number of odd elements = 2
|Number of even elements - Number of odd elements| = |2 - 2| = 0

Explanation 2:

For 1st test case:
The array is [2, 3, 5, 1].
Number of even elements = 1
Number of odd elements = 3
|Number of even elements - Number of odd elements| = |1 - 3| = |-2| = 2.

For 2nd test case:
The array is [4]
Number of even elements = 1
Number of odd elements = 0
|Number of even elements - Number of odd elements| = |1 - 0| = |1| = 1

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
26
# Initialize counters for even and odd elements
even_count = 0
odd_count = 0

# Iterate through the array
for num in arr:
# Check if the number is even
if num % 2 == 0:
even_count += 1
odd_count += 1

# Calculate the absolute difference

## Solution

See `Solution.py` for the implementation.