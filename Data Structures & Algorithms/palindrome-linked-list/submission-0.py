# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        stack = []

        self.addIntoStack(head, stack)

        node = head

        while node:
            if node.val != stack.pop():
                return False
            
            node = node.next

        return True
    

    def addIntoStack(self, node, stack):
        if not node:
            return
        
        stack.append(node.val)

        return self.addIntoStack(node.next, stack)