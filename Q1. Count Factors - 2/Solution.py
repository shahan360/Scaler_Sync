import math
class Solution:
    def solve(self, A):
        c = 0
        for i in range(1, int(math.sqrt(A))+1):
            if A%i==0:
                if (i==A/i):
                    c+=1
                    c+=2
        return c