# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, cur = None, head
        if not head:
            return None
        while cur:
            nxt_ptr = cur.next
            cur.next = prev
            prev = cur
            cur = nxt_ptr

        return prev
        
