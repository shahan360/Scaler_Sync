class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            Aleft = A[i-1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j-1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) // 2
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1
        return 0  # Edge case fallback