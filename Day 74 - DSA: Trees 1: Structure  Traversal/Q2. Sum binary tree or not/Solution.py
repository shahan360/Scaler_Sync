# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        # Helper to return sum of subtree rooted at node
        def subtree_sum(node):
            if node is None:
                return 0
            return node.val + subtree_sum(node.left) + subtree_sum(node.right)
        
        # Function that checks the sum tree property at every node
        def is_sum_tree(node):
            if node is None or (node.left is None and node.right is None):
                return True 
            
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            # Check current node value
            if node.val != left_sum + right_sum:
                return False

            # Recursively check left and right
            return is_sum_tree(node.left) and is_sum_tree(node.right)
        
        return 1 if is_sum_tree(A) else 0
