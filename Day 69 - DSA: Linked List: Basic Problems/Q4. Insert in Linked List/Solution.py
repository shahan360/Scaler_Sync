# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):
        new_node = ListNode(B)

        # Agar position 0 par insert karna hai (head par)
        if C == 0:
            new_node.next = A 
            return new_node 
        
        current = A 
        count = 0 

        # Traverse karo C-1 position tak, ya jab tak list khatam na ho jaaye 
        while current is not None and count < C - 1:
            current = current.next 
            count += 1 
        

        # Agar current None ho gayaa, toh list ki tail par add karna hai
        if not current:
            # Find tail and add (edge case if A is None)
            if not A:
                return new_node 
            temp = A 
            while temp.next:
                temp = temp.next 
            temp.next = new_node 
        else:
            # Insert node at position C 
            new_node.next = current.next 
            current.next = new_node
        
        return A
