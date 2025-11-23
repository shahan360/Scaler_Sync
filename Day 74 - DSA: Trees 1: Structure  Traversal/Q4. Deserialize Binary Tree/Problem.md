Problem Name: Q4. Deserialize Binary Tree

## Problem Description

Attempted
HINT SUPPORT
Hint 1
View
Solution Approach
View
Video Explanation
Rate Now
View
Complete Solution
Seen
View
Note : Points get deducted only when you unlock complete solution - 50% Point Reduction
Remember!

You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout Sample Codes for more details.

TEACHING ASSISTANT (TA) - HELP REQUEST
When can I access TA - Help Requests?
Solve problems on your own first. This will deepen your understanding of the topics and increase your confidence. Use the free hints provided by your instructors if you get stuck. TAs are here to help, but you'll learn best by trying to solve problems on your own. Hence, TA Help Requests will be accessible to you only after you use all the 'free hints' available for the problem.
Which type of Help Request should I make and how?
Refer to the video guide on raising TA Help Request'
Play
00:00 / 01:36
2x
21
22
23
24
25
26
27
28
20
17
18
19
29
14
15
16
11
12
13
4
5
6
7
10
8
9
continue
val_left = A[i]
val_right = A[i+1]
i += 2
if(val_left == -1):
cur.left = None
cur.left = TreeNode(val_left)
if(cur == None):
i = 1
while(len(q) != 0):
cur = q.popleft()
if(val_right == -1):
root = TreeNode(A[0])
q = deque()
q.append(root)
# @param A : list of integers
# @return the root node in the tree
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(10**6)
> Ongoing!
Test

## Input Format

, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout Sample Codes for more details.

TEACHING ASSISTANT (TA) - HELP REQUEST
When can I access TA - Help Requests?
Solve problems on your own first. This will deepen your understanding of the topics and increase your confidence. Use the free hints provided by your instructors if you get stuck. TAs are here to help, but you'll learn best by trying to solve problems on your own. Hence, TA Help Requests will be accessible to you only after you use all the 'free hints' available for the problem.
Which type of Help Request should I make and how?
Refer to the video guide on raising TA Help Request'
Play
00:00 / 01:36
2x
21
22
23
24
25
26
27
28
20
17
18
19
29
14
15
16
11
12
13
4
5
6
7
10
8
9
continue
val_left = A[i]
val_right = A[i+1]
i += 2
if(val_left == -1):
cur.left = None
cur.left = TreeNode(val_left)
if(cur == None):
i = 1
while(len(q) != 0):
cur = q.popleft()
if(val_right == -1):
root = TreeNode(A[0])
q = deque()
q.append(root)
# @param A : list of integers
# @return the root node in the tree
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(10**6)
> Ongoing!
Test

## Output Format

, instead return values as specified. Still have a question? Checkout Sample Codes for more details.

TEACHING ASSISTANT (TA) - HELP REQUEST
When can I access TA - Help Requests?
Solve problems on your own first. This will deepen your understanding of the topics and increase your confidence. Use the free hints provided by your instructors if you get stuck. TAs are here to help, but you'll learn best by trying to solve problems on your own. Hence, TA Help Requests will be accessible to you only after you use all the 'free hints' available for the problem.
Which type of Help Request should I make and how?
Refer to the video guide on raising TA Help Request'
Play
00:00 / 01:36
2x
21
22
23
24
25
26
27
28
20
17
18
19
29
14
15
16
11
12
13
4
5
6
7
10
8
9
continue
val_left = A[i]
val_right = A[i+1]
i += 2
if(val_left == -1):
cur.left = None
cur.left = TreeNode(val_left)
if(cur == None):
i = 1
while(len(q) != 0):
cur = q.popleft()
if(val_right == -1):
root = TreeNode(A[0])
q = deque()
q.append(root)
# @param A : list of integers
# @return the root node in the tree
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(10**6)
> Ongoing!
Test

## Example Explanation

Rate Now
View
Complete Solution
Seen
View
Note : Points get deducted only when you unlock complete solution - 50% Point Reduction
Remember!

You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout Sample Codes for more details.

TEACHING ASSISTANT (TA) - HELP REQUEST
When can I access TA - Help Requests?
Solve problems on your own first. This will deepen your understanding of the topics and increase your confidence. Use the free hints provided by your instructors if you get stuck. TAs are here to help, but you'll learn best by trying to solve problems on your own. Hence, TA Help Requests will be accessible to you only after you use all the 'free hints' available for the problem.
Which type of Help Request should I make and how?
Refer to the video guide on raising TA Help Request'
Play
00:00 / 01:36
2x
21
22
23
24
25
26
27
28
20
17
18
19
29
14
15
16
11
12
13
4
5
6
7
10
8
9
continue
val_left = A[i]
val_right = A[i+1]
i += 2
if(val_left == -1):
cur.left = None
cur.left = TreeNode(val_left)
if(cur == None):
i = 1
while(len(q) != 0):
cur = q.popleft()
if(val_right == -1):
root = TreeNode(A[0])
q = deque()
q.append(root)
# @param A : list of integers
# @return the root node in the tree
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(10**6)
> Ongoing!
Test

## Solution

See `Solution.py` for the implementation.