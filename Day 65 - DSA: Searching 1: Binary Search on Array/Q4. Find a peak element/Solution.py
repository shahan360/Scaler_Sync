class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low, high = 0, len(A) - 1
        
        while low < high:
            mid  = (low + high) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return A[low]