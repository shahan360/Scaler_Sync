from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        n = len(A)
        if B > n or B == 0:
            return []

        q = deque()  # store indices of useful elements for each window
        result = []

        for i in range(n):
            # Remove elements out of this window
            while q and q[0] <= i - B:
                q.popleft()

            # Remove elements smaller than current from the deque
            while q and A[q[-1]] < A[i]:
                q.pop()

            q.append(i)

            # The front element is the largest for the current window
            if i >= B - 1:
                result.append(A[q[0]])

        return result
