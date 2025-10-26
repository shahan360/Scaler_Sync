class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        alpha_count = 0
        digit_count = 0

        for ch in A:
            if ch.isalpha():
                alpha_count += 1
            elif ch.isdigit():
                digit_count += 1 
        
        return max(alpha_count, digit_count)
