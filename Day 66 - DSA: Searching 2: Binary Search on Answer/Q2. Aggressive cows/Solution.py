class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def can_place_cows(self, A, B, dist):
        count = 1
        last = A[0]
        for i in range(1, len(A)):
            if A[i] - last >= dist:
                count += 1
                last = A[i]
                if count == B:
                    return True
        return False

    def solve(self, A, B):
        A.sort()
        low, high = 0, A[-1] - A[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.can_place_cows(A, B, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
