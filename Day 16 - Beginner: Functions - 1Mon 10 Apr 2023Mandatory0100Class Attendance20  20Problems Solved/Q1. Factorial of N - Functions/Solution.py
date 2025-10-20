class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        fact = 1
        for i in range(1,A+1):
            fact = fact*i
        return fact    
