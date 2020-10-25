# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head is not None and head.next is not None:
            new_head = head.next
            prev.next = new_head
            temp = new_head.next
            new_head.next = head
            head.next = None
            prev = head
            head = temp
        if head is not None:
            prev.next = head
        return dummy.next
        
