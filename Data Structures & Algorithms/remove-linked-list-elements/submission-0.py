# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        return self.remover(head, val)

    

    def remover(self, node, val):
        if not node:
            return None
        
        node.next = self.remover(node.next, val)
        
        if node.val == val:
            return node.next
        
        return node
