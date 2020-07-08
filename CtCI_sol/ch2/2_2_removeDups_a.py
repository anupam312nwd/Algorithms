""" to remove duplicates from an unsorted linked list
in this code: creating a new LinkedList and changing that while keeping the old one """

# first write linkedlist class and node class
# use set to keep track of unique elements in the linkedlist
# use .remove() to remove elements from linkedlist

class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList():

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


def remove_dups(linklist):

    list_set = set()               # starting with empty set
    llist = SLinkedList()
    pointer = linklist.head

    while pointer is not None:
        if pointer.data in list_set:
            pointer = pointer.next
        else:
            llist.add(pointer.data)
            list_set.add(pointer.data)
            pointer = pointer.next
            print(llist)


link = SLinkedList()

link.add('r')
link.add('a')
link.add('a')
link.add('b')
link.add('b')
link.add('a')
link.add('b')
link.add('b')
link.add('b')
link.add('b')
link.add('c')
link.add('t')
link.add('c')

print(remove_dups(link))
