class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def can_paint(self, C, A, B, max_time):
        painters = 1
        time_sum = 0

        for length in C:
            time_sum += length
            if time_sum * B > max_time:
                painters += 1
                time_sum = length
                if painters > A:
                    return False
        return True

    def paint(self, A, B, C):
        MOD = 10000003
        low = max(C) * B
        high = sum(C) * B
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if self.can_paint(C, A, B, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans % MOD

