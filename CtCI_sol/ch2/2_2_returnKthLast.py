
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList():

    def __init__(self, head=None):
        self.head = None

    def add(self, k):
        node = Node(k)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

def k_last(link, k):
    lst = []
    p = link.head
    while p is not None:
        lst.append(p)
        p = p.next

    return lst[-k]


link = SLinkedList()

link.add('r')
link.add('g')
link.add('c')
link.add('a')
link.add('m')
link.add('t')

print(k_last(link, 2).data)
print(k_last(link, 3).data)
print(k_last(link, 4).data)
