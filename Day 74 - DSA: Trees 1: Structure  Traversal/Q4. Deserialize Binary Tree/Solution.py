# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        if not A or A[0] == -1:
            return None

        root = TreeNode(A[0])
        queue = [root]
        i = 1

        while queue and i < len(A):
            current = queue.pop(0)

            # Left child
            if i < len(A):
                if A[i] != -1:
                    current.left = TreeNode(A[i])
                    queue.append(current.left)
                else:
                    current.left = None
                i += 1

            # Right child
            if i < len(A):
                if A[i] != -1:
                    current.right = TreeNode(A[i])
                    queue.append(current.right)
                else:
                    current.right = None
                i += 1

        return root

