class Solution:
    # @param A : long
    # @return an integer
    def solve(self, A):
        # i = 1
        # if A<=1:
        #     return 0
        # for i in range(2,int(math.sqrt(A)+1)):
        #     if A%i==0:
        #         return 0
        # return 1   
        
        #Brute Force Code
        # if A<=1:
        #     return 0
        # for i in range(2,A):
        #     if A%i==0:
        #         return 0
        # return 1 

        #optimized Code
        # i = 1
        # if A<=1:
        #     return 0
        # for i in range(2,int(math.sqrt(A))+1):
        #     if A%i==0:
        #         return 0
        # return 1  
        def isfactors(A):
            c = 0
            for i in range(1,int(math.sqrt(A))+1):
                if A%i==0:
                    if i==A//i:
                        c+=1
                    else:
                        c+=2
            return c 
        if isfactors(A)==2:
            return 1
        else:
            return 0                                                     