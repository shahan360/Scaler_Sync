Problem Name: Q4. HCF - Easy

Q4. HCF - Easy
Solved
Problem Description
Write a program to input two integers A & B from user and print their HCF.
Definition Of HCF: The HCF(Highest Common Factor) or the GCD(greatest common divisor) of two positive integers happens to be the largest positive integer that divides the numbers without leaving a remainder.
Problem Constraints
1 <= A,B <= 100000
Input Format
First line will contain 2 integers A and B
Output Format
An integer which is the HCF of A & B.
Example Input
Input 1:
15 105 
Input 2:
24 36 
Example Output
Output 1:
15
Output 2:
12
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
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    C = list(map(int,input().split()))
    A = C[0]
    B = C[1]
    while B>0:
        A,B = B,A%B
    print(A)        
    return 0
if __name__ == '__main__':
    main()
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 13 - Beginner: Iterations : Loop - 2
Day 15 - Beginner: Iterations - Patterns

## Problem Constraints

1 <= A,B <= 100000

## Input Format

First line will contain 2 integers A and B

## Output Format

An integer which is the HCF of A & B.

## Solution

See `Solution.py` for the implementation.