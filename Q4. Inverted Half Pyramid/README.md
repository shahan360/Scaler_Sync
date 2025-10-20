Problem Name: Q4. Inverted Half Pyramid

Q4. Inverted Half Pyramid
Solved
No.	Time	Status	Runtime	Language
1
	19 Oct 2025, Sun, 6:17 PM	
Correct Answer
	211 ms	Python 3 (python-3.8)
2
	19 Apr 2025, Sat, 6:28 PM	
Correct Answer
	190 ms	Python 3 (python-3.8)
3
	7 Dec 2024, Sat, 10:10 PM	
Correct Answer
	180 ms	Python 3 (python-3.8)
4
	3 Jun 2023, Sat, 6:27 PM	
Correct Answer
	1036 ms	Java 8 (oracle-jdk-1.8)
5
	8 Apr 2023, Sat, 6:59 PM	
Correct Answer
	1051 ms	Java 8 (oracle-jdk-1.8)
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
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(1, N+1):
        for j in range(1,N+2-i):
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

## Solution

See `Solution.py` for the implementation.