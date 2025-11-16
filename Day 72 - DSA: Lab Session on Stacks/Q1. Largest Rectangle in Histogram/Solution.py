class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
        stack = []
        max_area = 0
        index = 0

        while index < len(A):
            # If current bar is higher than bar at stack top or stack is empty, push it
            if not stack or A[index] >= A[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Calculate area with bar at the top of stack as the smallest bar
                top_of_stack = stack.pop()
                # If stack is empty means all bars before index are higher
                width = index if not stack else index - stack[-1] - 1
                area = A[top_of_stack] * width
                max_area = max(max_area, area)

        # Remaining bars in stack
        while stack:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = A[top_of_stack] * width
            max_area = max(max_area, area)

        return max_area