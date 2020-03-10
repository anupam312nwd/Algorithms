""" Codes for Single Linked List data structure """

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, k):
        """ add """
        node = Node(k)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, k):
        p = self.head
        while p != None:
            if (p.data == k):
                return True
            p = p.next
        return False

    def remove(self, k):
        p = self.head
        if p.data == k:
            self.head = p.next
            return None
        while p.next != None:
            if (p.next.data == k):
                p.next = p.next.next
                return None
            p = p.next
        return None

    def __str__(self):
        """ to define self print output """
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data + "->"
                p = p.next
            s += p.data
        return s

l = SLinkedList()

l.add('a')
l.add('b')
l.add('c')
l.add('r')
l.add('a')
l.add('e')
l.add('t')

print(l)
# l.remove(l.search('t'))
l.remove('t')
print(l)
l.remove('r')
print(l)
l.remove('a')
print(l)
print(l.search('c'))
print(l.search('z'))

