
# Create Linked List-append (create nodes with positive and negative numbers)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

n = int(input("Enter the no of Nodes: "))
head = None

for i in range(n):
    data = int(input("enter the values"))
    head = append(head, data)

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print(None)
