# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        temp = A
        result = []
        while temp is not None:
            result.append(str(temp.val))
            temp = temp.next
        # Join the values with space and print once
        print(" ".join(result)+" ")
            

