
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self, head=None):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove_next(self, data):
        self.next = self.next.next

    def __repr__(self):
        s = ""
        pointer = self.head
        if pointer is None: return s
        while pointer.next is not None:
            s += pointer.data + "->"
            pointer = pointer.next
        s += pointer.data
        return s



link = SLinkedList()

link.add('a')
link.add('b')
link.add('c')
link.add('d')
link.add('c')
link.add(None)

print(link)
pointer = link.head
print(pointer)
print()
