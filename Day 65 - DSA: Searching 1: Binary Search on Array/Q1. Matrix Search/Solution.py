class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        # Brute Force Approach
        # for row in A:
        #     for val in row:
        #         if val == B:
        #             return 1
        # return 0

        # Binary Search Approach
        N = len(A)
        M = len(A[0])
        low, high = 0, N * M - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // M 
            col = mid % M 
            if A[row][col] == B:
                return 1 
            elif A[row][col] < B:
                low = mid + 1
            else:
                high = mid - 1
        return 0
