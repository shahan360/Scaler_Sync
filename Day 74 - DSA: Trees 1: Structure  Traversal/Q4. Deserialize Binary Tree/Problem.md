Problem Name: Q4. Deserialize Binary Tree

## Problem Description

Attempted
No.	Time	Status	Runtime	Language

1
23 Nov 2025, Sun, 1:43 AM
Runtime Error

2
23 Nov 2025, Sun, 1:42 AM
Runtime Error

3
23 Nov 2025, Sun, 1:41 AM
Runtime Error
20
21
22
23
24
25
26
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
16
17
18
19
1
2
current = queue.pop(0)
# Assign left child
if A[i] != -1:
current.left = TreeNode(A[i])
queue.append(current.left)
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
# @param A : list of integers
# @return the root node in the tree
if not A or A[0] == -1:

## Solution

See `Solution.py` for the implementation.