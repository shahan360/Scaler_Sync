Problem Name: Q3. Stair Pattern

Q3. Stair Pattern
Solved
No.	Time	Status	Runtime	Language
1
	19 Oct 2025, Sun, 3:59 PM	
Correct Answer
	103 ms	Python 3 (python-3.8)
2
	19 Oct 2025, Sun, 2:21 PM	
Correct Answer
	111 ms	Python 3 (python-3.8)
3
	19 Oct 2025, Sun, 2:21 PM	
Correct Answer
	105 ms	Python 3 (python-3.8)
4
	19 Oct 2025, Sun, 2:14 PM	
Correct Answer
	110 ms	Python 3 (python-3.8)
5
	19 Oct 2025, Sun, 1:49 PM	
Correct Answer
	109 ms	Python 3 (python-3.8)
6
	19 Apr 2025, Sat, 6:25 PM	
Correct Answer
	98 ms	Python 3 (python-3.8)
7
	7 Dec 2024, Sat, 10:08 PM	
Correct Answer
	108 ms	Python 3 (python-3.8)
8
	3 Jun 2023, Sat, 6:20 PM	
Correct Answer
	511 ms	Java 8 (oracle-jdk-1.8)
9
	8 Apr 2023, Sat, 6:57 PM	
Correct Answer
	527 ms	Java 8 (oracle-jdk-1.8)
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

## Solution

See `Solution.py` for the implementation.