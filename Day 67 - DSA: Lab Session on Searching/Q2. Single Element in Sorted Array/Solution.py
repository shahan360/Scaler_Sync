class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even for pairing check
            if mid % 2 == 1:
                mid -= 1
            if A[mid] == A[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return A[low]