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
        if pointer is None:
            return s
        while pointer.next is not None:
            s += pointer.data + "->"
            pointer = pointer.next
        s += pointer.data
        return s


def remove_dups(linklist):

    list_set = set()  # starting with empty set
    # llist = SLinkedList()
    pointer = linklist.head
    list_set.add(pointer.data)

    while pointer.next is not None:
        print(linklist)
        print(list_set)
        if pointer.next.data in list_set:
            if pointer.next.next is None:
                pointer.next = None
                return linklist
            else:
                pointer.next.data = pointer.next.next.data
                pointer.next = pointer.next.next
        else:
            # list_set.add(pointer.data)
            list_set.add(pointer.next.data)
            pointer = pointer.next
    return linklist


link = SLinkedList()


link.add("r")
link.add("r")
link.add("a")
link.add("a")
link.add("b")
link.add("b")
link.add("a")
link.add("b")
link.add("b")
link.add("b")
link.add("b")
link.add("c")
link.add("t")

# link.add('c')
# link.add('d')
# link.add('c')
# link.add('a')
# link.add('a')
# link.add('a')
# link.add('b')
# link.add('t')

print("-------------------------------------------------- ")
print("final list", remove_dups(link))
