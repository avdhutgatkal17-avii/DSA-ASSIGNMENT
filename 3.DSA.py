
# 3.Insert node at a specific position

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
head = a
a.next = b
b.next = c
c.next = d

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print(None)

current = head

n = int(input("Position to insert a number"))
new_node = Node(int(input("Enter the node")))

current = head
for i in range(n):
    if i == (n - 2):
        new_node.next = current.next
        current.next = new_node
    current = current.next

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print(None)
