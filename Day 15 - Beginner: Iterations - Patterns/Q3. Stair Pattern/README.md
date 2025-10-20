Problem Name: Q3. Stair Pattern

Q3. Stair Pattern
Solved
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
Using hints except Complete Solution is Penalty free now
Use Hint

Problem Description

Take an integer N as input, print the corresponding stair pattern for N.

For example if N = 4 then stair pattern will be like:

*
**
***
****

Problem Constraints

1 <= N <= 100

Input Format

First and only line of input contains a single integer N.

Output Format

Output the stair pattern corresponding to the given N.

Example Input

Input 1:

2

Input 2:

3

Example Output

Output 1:

*
**

Output 2:

*
**
***

Example Explanation

Print the pattern as described.

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
for i in range(1,N+1):
for j in range(i):
print("*",end="")
print("")
return 0
if __name__ == '__main__':
main()
Test Output
Output goes here..Test/Submit
TestTest With Custom Input
Submit
Day 14 - Beginner: Iterations : Loop - 3
Day 16 - Beginner: Functions - 1
2X Rewards
Referral rewards just got DOUBLED!
Earn
12000
₹25,000
on your 1st Referral
Refer and Earn
All modules, classes and certifications
All career related classes and 1-1 mentor sessions
Earn skill certificate to unlock job opportunities
New
Day 15 - Beginner: Iterations - Patterns
Fri, 7 Apr 2023
Mandatory
0

100%
Class Attendan

## Solution

See `Solution.py` for the implementation.