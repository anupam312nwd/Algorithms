""" Codes for Single Linked List data structure """


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def add(self, k):
        """ add """
        node = Node(k)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, k):
        p = self.head
        while p is not None:
            if (p.data == k):
                return True
            p = p.next
        return False

    def remove(self, k):
        p = self.head
        if p.data == k:
            self.head = p.next
            return None
        while p.next is not None:
            if (p.next.data == k):
                p.next = p.next.next
                return None
            p = p.next
        return None

    def __repr__(self):
        """ to define self print output """
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += p.data + "->"
                p = p.next
            s += p.data
        return s


Link = SLinkedList()

Link.add('a')
Link.add('b')
Link.add('c')
Link.add('r')
Link.add('a')
Link.add('e')
Link.add('t')

print(Link)
# Link.remove(Link.search('t'))
Link.remove('t')
print(Link)
Link.remove('r')
print(Link)
Link.remove('a')
print(Link)
print(Link.search('c'))
print(Link.search('z'))
