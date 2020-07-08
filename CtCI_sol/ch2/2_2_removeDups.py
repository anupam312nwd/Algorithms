""" to remove duplicates from an unsorted linked list """

# first write linkedlist class and node class
# use set to keep track of unique elements in the linkedlist
# use .remove() to remove elements from linkedlist

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


def remove_dups(llist):

    list_set = set()               # starting with empty set
    pointer = llist.head

    while pointer is not None:
        # print(list_set)
        if pointer.data in list_set:
            # if pointer.next is not None:
            pointer.data = pointer.next.data
            pointer.next = pointer.next.next
            # else:
            #     pointer.data = None
            #     pointer.next = None
        else:
            list_set.add(pointer.data)
            pointer = pointer.next
        print(llist)
        print(pointer.data)
    return llist


link = SLinkedList()

link.add('a')
link.add('b')
link.add('c')
link.add('d')
link.add('c')
link.add('a')
link.add('c')
link.add('a')
link.add('b')
link.add('t')

print(link)
print(remove_dups(link))
