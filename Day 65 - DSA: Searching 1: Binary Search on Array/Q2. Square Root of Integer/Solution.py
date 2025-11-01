class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low, high = 0, A
        ans = 0
        while low <= high:
            mid  = (low + high) // 2
            square = mid * mid

            if square == A:
                return mid
            elif square < A:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1
        return ans
        
