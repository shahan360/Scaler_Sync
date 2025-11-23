Problem Name: Q4. Deserialize Binary Tree

## Problem Description

Attempted
No.	Time	Status	Runtime	Language

1
23 Nov 2025, Sun, 1:45 AM
Runtime Error

2
23 Nov 2025, Sun, 1:43 AM
Runtime Error

3
23 Nov 2025, Sun, 1:42 AM
Runtime Error

4
23 Nov 2025, Sun, 1:41 AM
Runtime Error
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
26
27
28
29
30
31
32
33
34
35
root = TreeNode(A[0])
queue = [root]
i = 1
while queue and i < len(A):
current = queue.pop(0)
# Left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
i += 1
# Right child
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
i += 1

## Solution

See `Solution.py` for the implementation.