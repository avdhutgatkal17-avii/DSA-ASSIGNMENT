# 4.Delete the nodes having negative values

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(-30)
d = Node(40)
head = a
a.next = b
b.next = c
c.next = d
current = head

while current is not None:
    if current.data < 0:
        current = current.next
        continue
    print(current.data, end="->")
    current = current.next

print(None)
