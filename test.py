# code taken from here: https://gist.github.com/ptigas/2820165
# testing the change
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head = None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if p.data == k:
                    return p
                p = p.next
            if p.data == k:
                return p
        return None

    def remove(self, p):
        # p = l.search(p)
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next is not None:
                s += p.data
                p = p.next
            s += p.data
        return s


# example code
l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')

print(l)
l.remove(l.search('b'))
# l.remove('b')
print(l)
