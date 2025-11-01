class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        res = []
        for i in range(len(A)):
            if A[i] == B:
                res.append(i)
        if not res:
            return [-1, -1]
        return [min(res), max(res)]
