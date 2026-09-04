# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False

        node = head 
        arr = []
        while node.next != None: 
            if node.val == 1001: 
                return True
            node.val = 1001
            node = node.next
        return False
            
