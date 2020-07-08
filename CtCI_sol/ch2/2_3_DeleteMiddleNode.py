
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList():
    def __init__(self, head=None):
        self.head = head

    def add(self, k):
        node = Node(k)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def DeleteAccessedNode(self, pointer):
        pointer.data = pointer.next.data
        pointer.next = pointer.next.next

    def __repr__(self):
        s = ""
        pointer = self.head
        s += pointer.data
        while pointer.next is not None:
            s += "->" + pointer.next.data
            pointer = pointer.next
        return s


link = SLinkedList()
link.add('a')
link.add('b')
link.add('c')
link.add('d')
link.add('e')

print(link)
pointer = link.head.next.next.next
link.DeleteAccessedNode(pointer)
print(link)
print(link.head.data)
