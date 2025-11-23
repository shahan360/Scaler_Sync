Problem Name: Q4. Deserialize Binary Tree

## Problem Description

Attempted
No.	Time	Status	Runtime	Language

1
23 Nov 2025, Sun, 1:41 AM
Runtime Error
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
i = 1
while queue and i < len(A):
current = queue.pop(0)
# Assign left
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
i += 1
# Assign right
if A[i] != -1:
current.right = TreeNode(A[i])
queue.append(current.right)
i += 1

## Solution

See `Solution.py` for the implementation.