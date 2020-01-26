## Contains bugs
## Not working

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, k):
        p = self.head
        while p != None:
            if (p.data == k):
                return p
            p = p.next
        return None

    def remove(self, k):
        p = self.head
        if p == k:
            self.head = None
        while p.next != None:
            if (p.next == k):
                p.next = p.next.next
                return p
            p = p.next
        return 'notgood'

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s

l = SLinkedList()

l.add('a')
l.add('b')
l.add('c')
l.add('r')
l.add('e')
l.add('t')

print(l)
# l.remove(l.search('e'))
print(l.remove('r'))
print(l)
print(l.search('r'))
print('r'.next)
