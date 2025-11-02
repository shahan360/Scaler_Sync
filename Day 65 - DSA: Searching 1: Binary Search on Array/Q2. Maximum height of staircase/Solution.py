class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        height  = 0
        remaining_blocks = A 
        while remaining_blocks >= (height + 1):
            height += 1
            remaining_blocks -= height
        return height
