class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        paren_map = {')':'(','}':'{',']':'['}
        for char in A:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != paren_map[char]:
                    return 0
                stack.pop()
        return 1 if not stack else 0
