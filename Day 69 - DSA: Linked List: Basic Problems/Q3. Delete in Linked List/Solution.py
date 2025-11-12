# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        # Agar first node delete karna hai (B==0)
        if B == 0:
            return A.next 
        
        # Otherwise, B-th node delete karna hai 
        current = A 
        count = 0 

        # B-1 position tak jaao 
        while count < B-1 and current:
            current = current.next 
            count += 1
        
        # current ab B-1-th node par hai, uske baad waala node delete karna hai
        if current and current.next:
            current.next = current.next.next 
        
        return A
