Problem Name: Q3. Numeric Stair Pattern

Q3. Numeric Stair Pattern
Solved
No.	Time	Status	Runtime	Language
1
	19 Oct 2025, Sun, 10:06 PM	
Correct Answer
	114 ms	Python 3 (python-3.8)
2
	19 Oct 2025, Sun, 9:48 PM	
Correct Answer
	109 ms	Python 3 (python-3.8)
3
	20 Apr 2025, Sun, 3:19 AM	
Correct Answer
	103 ms	Python 3 (python-3.8)
4
	10 Apr 2023, Mon, 12:30 AM	
Correct Answer
	522 ms	Java 8 (oracle-jdk-1.8)
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
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(1,N+1):
        print(" ".join(str(j) for j in range(1, i+1)))    
    return 0
if __name__ == '__main__':
    main()
Test Output
Please wait while we are evaluating
Compiling your Code...
> Success!
TestTest With Custom Input
Submit
Day 14 - Beginner: Iterations : Loop - 3
Day 16 - Beginner: Functions - 1
✓ Successfully synced to GitHub!

## Solution

See `Solution.py` for the implementation.