class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        stack = []
        result = []
        for num in A:
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(num)
        return result
