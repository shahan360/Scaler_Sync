Problem Name: Q6. Two Line Star Pattern

Q6. Two Line Star Pattern
Solved
No.	Time	Status	Runtime	Language
1
	19 Oct 2025, Sun, 10:24 PM	
Correct Answer
	97 ms	Python 3 (python-3.8)
2
	24 Oct 2023, Tue, 4:54 AM	
Correct Answer
	106 ms	Python 3 (python-3.8)
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
    for i in range(N):
        print("*", end='') # Print the first asterisk without a newline
        for j in range(N-2):
            print(" ",end='') # Print spaces without a newline
        print("*") # Print the last asterisk with a newline     
    return 0
if __name__ == '__main__':
    main()
Test Output
Output goes here..Test/Submit
TestTest With Custom Input
Submit
Day 14 - Beginner: Iterations : Loop - 3
Day 16 - Beginner: Functions - 1

## Solution

See `Solution.py` for the implementation.