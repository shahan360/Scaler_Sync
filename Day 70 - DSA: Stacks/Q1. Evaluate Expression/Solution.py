class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        stack = []
        for token in A:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
        return stack[0]
