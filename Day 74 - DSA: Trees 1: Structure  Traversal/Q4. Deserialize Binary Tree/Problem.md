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
50% points reduction
Unlock
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
27
28
29
30
31
32
33
34
35
36
37
38
39
while queue and i < len(A):
current = queue.pop(0)
# Left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
current.left = None
i += 1
# Right child
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
current.right = None
i += 1

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
27
28
29
30
31
32
33
34
35
36
37
38
39
while queue and i < len(A):
current = queue.pop(0)
# Left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
current.left = None
i += 1
# Right child
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
current.right = None
i += 1

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
27
28
29
30
31
32
33
34
35
36
37
38
39
while queue and i < len(A):
current = queue.pop(0)
# Left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
current.left = None
i += 1
# Right child
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
current.right = None
i += 1

## Example Explanation

Rate Now
View
Complete Solution
50% points reduction
Unlock
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
27
28
29
30
31
32
33
34
35
36
37
38
39
while queue and i < len(A):
current = queue.pop(0)
# Left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
current.left = None
i += 1
# Right child
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
current.right = None
i += 1

## Solution

See `Solution.py` for the implementation.