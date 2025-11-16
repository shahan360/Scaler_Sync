class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = []
        result = [-1] * len(A)
        for i, num in enumerate(A):
            while stack and A[stack[-1]] < num:
                idx = stack.pop()
                result[idx] = num
            stack.append(i)
        return result