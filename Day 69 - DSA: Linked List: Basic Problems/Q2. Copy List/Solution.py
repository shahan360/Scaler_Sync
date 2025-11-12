# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None 
        
        # Step 1: Har node ke baad uska copy node insert karo
        current = head 
        while current is not None:
            copy = RandomListNode(current.label)
            copy.next = current.next 
            current.next = copy 
            current = copy.next 
        # 1->1'->2->2'->3->3'

        # Step 2: Copy node ke random pointers set karo 
        current = head 
        while current is not None:
            if current.random is not None:
                current.next.random = current.random.next 
            current = current.next.next 
        
        # Step 3: Alag alag lists banao (original and copy)
        original = head
        copy_head = head.next 
        copy = copy_head 
        while original and copy:
            original.next = copy.next
            original = original.next
            if original:
                copy.next = original.next 
                copy = copy.next 
        return copy_head

        
