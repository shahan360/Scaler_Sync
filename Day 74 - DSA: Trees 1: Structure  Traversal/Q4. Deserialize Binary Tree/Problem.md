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
19
20
21
22
23
24
25
26
18
15
16
17
27
28
29
30
31
32
33
34
35
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
cur.right = None
cur.right = TreeNode(val_right)
q.append(cur.left)
q.append(cur.right)

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
19
20
21
22
23
24
25
26
18
15
16
17
27
28
29
30
31
32
33
34
35
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
cur.right = None
cur.right = TreeNode(val_right)
q.append(cur.left)
q.append(cur.right)

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
19
20
21
22
23
24
25
26
18
15
16
17
27
28
29
30
31
32
33
34
35
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
cur.right = None
cur.right = TreeNode(val_right)
q.append(cur.left)
q.append(cur.right)

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
19
20
21
22
23
24
25
26
18
15
16
17
27
28
29
30
31
32
33
34
35
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
cur.right = None
cur.right = TreeNode(val_right)
q.append(cur.left)
q.append(cur.right)

## Solution

See `Solution.py` for the implementation.