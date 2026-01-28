# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dumy = ListNode(0)
        cur = dumy
        carry = 0

        while l1 or l2 or carry:
        
            # lets add 
            v1= l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry  
            carry = sum//10 # carry is quotient
            cur.next = ListNode(sum%10) # the digit to be placed is the remainder
        
            # move pointers forward
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dumy.next
