class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        a = ""
        for char in A:
            a += chr(ord(char)+32)
        
        return a

