Problem Name: Q6. Average Rainfall

## Problem Description

Create an array of size N, which can store rainfall size for N days.
Take rainfall measurement for N days from user and print floor of average rainfall for N days.

Note :
1. Rainfall measurement is non-decimal number.
2. For Floor of number use Math.Floor(NUM) function.
3. Average = (Sum of entries) / (number of entries)

## Problem Constraints

0 < N <= 10000
0<= arr[i] <= 50

## Input Format

1. In first argument, take N as size of array.
2. Take N entries then and store it in array of rainfall measurement.

## Output Format

Print floor of average rainfall in single line.

## Example Input

Input 1 :
10
Input 2 :
12

## Example Output

Output 1 :
25
Output 2 :
20

Example Explanation

## Example Explanation

Explanation 1 :
Rainfall measurement is 12 26 25 21 18 10 45 40 29 30,
Average rainfall is 25.6
Floor value of 25.6 is 25

Explanation 2 :
Rainfall measurement is 12 28 23 21 18 15 14 40 12 30 10 19,
Average rainfall is 20.166666
Floor value of 20.1666 is 20

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

## Solution

See `Solution.java` for the implementation.