# code taken from here: https://gist.github.com/ptigas/2820165


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
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
        # p = Llist.search(p)
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += p.data
                p = p.next
            s += p.data
        return s


# example code
Llist = DLinkedList()

Llist.add("a")
Llist.add("b")
Llist.add("c")
# added a new comment here

print(Llist)
print(Llist.search("b"))
Llist.remove(Llist.search("b"))
print(Llist)
