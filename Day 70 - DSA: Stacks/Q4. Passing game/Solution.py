class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        stack = [B]
        for val in C:
            if val == 0:
                stack.pop()
            else:
                stack.append(val)
        return stack[-1]
