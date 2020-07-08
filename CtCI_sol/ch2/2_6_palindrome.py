""" implement a function to check if a linked list is Palindrome """

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList():
    def __init__(self, head=None):
        self.head = head

    def add(self, k):
        node = Node(k)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return None

    def __repr__(self):
        s = ""
        pointer = self.head
        s += pointer.data

        while pointer.next is not None:
            s += "->" + pointer.next.data
            pointer = pointer.next
        return s

def checkPalindrome(link):
    str1 = ""
    str2 = ""
    pointer = link.head
    while pointer is not None:
        str1 = str1 + pointer.data
        str2 = pointer.data + str2
        pointer = pointer.next
    return str1 == str2


if __name__ == '__main__':

    link = SLinkedList()
    link.add('a')
    link.add('b')
    link.add('=')
    link.add('[')
    link.add('t')
    link.add('[')
    link.add('=')
    link.add('b')
    link.add('a')
    print(checkPalindrome(link))
    if checkPalindrome(link):
        print(link, "is palindrome")
    else:
        print(link, "is NOT palindrome")
