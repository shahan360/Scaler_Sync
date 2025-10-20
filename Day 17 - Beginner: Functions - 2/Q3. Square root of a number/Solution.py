class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sqrt = A**(1/2)
        sqrt2 = int(sqrt)
        if (sqrt2**2)==A:
            return sqrt2
        else:
            return -1
