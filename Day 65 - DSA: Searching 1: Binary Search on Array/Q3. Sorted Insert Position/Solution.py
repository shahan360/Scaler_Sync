class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        low, high  = 0, len(A) - 1
        ans = len(A)

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                return mid 
            elif A[mid] < B:
                low = mid + 1
            else:
                ans = mid 
                high = mid - 1

        return ans
