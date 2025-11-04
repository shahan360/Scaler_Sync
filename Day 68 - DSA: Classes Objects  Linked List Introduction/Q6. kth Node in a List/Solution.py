# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp = A
        for _ in range(0,B):
            if temp is None:
                return -1
            temp = temp.next
        if temp is None:
                return -1
        return temp.val