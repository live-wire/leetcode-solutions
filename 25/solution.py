# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         def validate(head,k):
#             if head==None:
#                 return False
#             while k>1:
#                 if head.next == None:
#                     return False
#                 else:
#                     head=head.next
#                     k=k-1
#             return True
        
#         def reverse(root,k):
#             leader=root
#             # temp = None
#             prev,curr,forward = None,root,None
#             print("reverse {} k {}".format(root,k))

#             while k>1:
#                 forward = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = forward
#                 k = k-1
#                 # print("curr {} k {}".format(curr,k))

#             root.next = curr
#             if curr is None:
#                 root = None
#             else:
#                 root = curr.next
#             # return root
#         if k<2:
#             return head
#         if not head:
#             return None
        
#         root = head
#         i=1
#         while validate(root,k):
#             reverse(root,k*i)
#             i=i+1
#             print("head {}".format(root))

#         return head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:     
        now  = head
        prev  = None
        group_count = 0
        prev_tail = dummy = ListNode(-999)
        prev_tail.next = head  # if size of entire list <k , return head 
        
        def reverse(prev,curr, k):
            last_head = curr
            while  k:
                temp = curr.next
                curr.next = prev
                prev = curr 
                curr = temp
                k -=1 
            return last_head, curr,prev
        def get_group_size(curr,n):
            k = 0
            while curr and k < n:
                curr = curr.next 
                k += 1
            return k
        while now and get_group_size(now, k) % k == 0:
            new_tail,now,prev = reverse(None, now, k)
            new_tail.next = now
            prev_tail.next =  prev
            prev_tail = new_tail
            group_count += 1         
        return  dummy.next
        
