class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
list1 = node1
# create another linked List
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n1.next = n2
n2.next = n3
list2 = n1
#create an empty head node
head = Node(0)
current = head
# print(head)
# merging two list
while list1 and list2:
    
    if list1.data < list2.data:
        current.next = list1
        list1 = list1.next
    else:
        current.next = list2
        list2 = list2.next
    
    current = current.next
    
current.next = list1 or list2

while head.next:
    head = head.next
    print(head.data, end=' ')
    




