class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        for row in A:
            for val in row:
                if val == B:
                    return 1
        return 0
