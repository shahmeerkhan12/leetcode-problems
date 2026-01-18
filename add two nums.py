# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        temp2 = l2

        dumy = ListNode(0)
        cur = dumy
        carry = 0

        while temp or temp2 or carry:
        
            # lets add 
            v1= temp.val if temp else 0
            v2 = temp2.val if temp2 else 0

            sum = v1 + v2 + carry  
            carry = sum//10 # carry is quotient
            cur.next = ListNode(sum%10) # the digit to be placed is the remainder
        
            # move pointers forward
            cur = cur.next
            if temp:
                temp = temp.next
            if temp2:
                temp2 = temp2.next

        return dumy.next
