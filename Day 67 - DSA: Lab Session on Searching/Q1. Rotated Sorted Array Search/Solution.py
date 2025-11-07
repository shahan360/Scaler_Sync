class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        low = 0
        high = len(A) - 1
        while(low<=high):
            mid = (low+high)//2
            if (A[mid]==B):
                return mid
            if (A[mid]>A[0]):
                if B<A[mid] and B>=A[0]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if B<=A[-1] and B>A[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
