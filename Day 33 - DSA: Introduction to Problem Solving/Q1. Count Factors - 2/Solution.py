import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c = 0
        # k = len(A);
            
        
        #Brute Force Case
        # for i in range(1,A+1):
        #     if A%i==0:
        #         c+=1
        # return c 
        
        #optimization case
        for i in range(1, int(math.sqrt(A))+1):
            if A%i==0:
                if (i==A/i):
                    c+=1
                else:
                    c+=2
        return c                                         






#### This is the end!