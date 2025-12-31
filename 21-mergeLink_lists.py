# Definition for singly-linked list.

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         head = ListNode(0)
#         current = head
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#         current.next  = list1 or list2

#         return head.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# create a linked list
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = None

# traversing linked list ITERATIVELY
head = n1
current = head
# while current:
#     print(current.val, end = " -> ")
#     current = current.next

# traversing by recursion
def recursion_(head):
    
    # if head is None
    if head is None:
        return
    
    # print the node data
    print(head.val, end='')

    #lets print some arrows too
    if head.next is not None:
        print(" -> ", end= " ")

    # make a reursive call with head.next
    recursion_(head.next)


recursion_(head)