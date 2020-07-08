""" want to create a SingleLinked List
then add some methods to that list:
add, search, remove, __str__ """

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self, head=None):
        self.head = None

    # def add(self, k):
    #     """ add a node in the beginning """
    #     node = Node(k)
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         node.next = self.head
    #         self.head = node

    def add_nodes(self, *args):
        """ add a node in the beginning """
        for k in args:
            node = Node(k)
            if self.head is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node

    def search(self, k):
        """ return True if exist in LinkedList else False """
        pointer = self.head
        while pointer is not None:
            if (pointer.data == k):
                return True
            else:
                pointer = pointer.next
        return False

    def appendToTail(self, k):
        """ add data k at the end of the List """
        pointer = self.head     # both pointer and self.head have same memory location
        if pointer is None:
            self.head = Node(k)
        else:
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = Node(k)
        return None

    def remove(self, k):
        """ find and remove first instance of k from the List """
        if self.head is None:
            return None
        pointer = self.head
        if pointer.data == k:
            self.head = pointer.next
            return None
        else:
            while pointer.next is not None:
                if pointer.next.data == k:
                    pointer.next = pointer.next.next
                    return None
                pointer = pointer.next
            return None

    def __repr__(self):
        """ define a pretty print functionality """
        s = ""
        pointer = self.head
        if pointer is None: return s
        while pointer.next is not None:
            s += pointer.data + " -> "
            pointer = pointer.next
        s += pointer.data
        return s

# link = SLinkedList()
# link.add('a')
# link.add('b')
# link.add('c')

# print(link)
# link.add('d')
# print(link)
# print(link.search('b'))
# link.remove('b')
# print('--------------------------------------------------')
# print(link)

print('-------------------------------------------------- ')
link1 = SLinkedList()
link1.add_nodes('a', 't', 'l', 'm', '[', '=', 'r')
print(link1)
