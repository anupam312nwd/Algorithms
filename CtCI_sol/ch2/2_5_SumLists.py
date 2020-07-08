""" input: two linked lists as integers st 1's digit at head of the list,
    output: sum of two numbers"""

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

    def __repr__(self):
        s = ""
        pointer = self.head
        s += pointer.data

        while pointer.next is not None:
            s += "->" + pointer.next.data
            pointer = pointer.next
        return s

    def get_num(self):
        pointer = self.head
        num = 0
        i = 0
        while pointer is not None:
            num += (10**i)*int(pointer.data)
            pointer = pointer.next
            i += 1
        return num

    def get_num_reverse(self):
        pointer = self.head
        s = ""
        while pointer is not None:
            s = s + pointer.data
            pointer = pointer.next
        return int(s)

def SumList(link1, link2):
    num1 = link1.get_num()
    num2 = link2.get_num()
    print(num1, num2)
    return num1 + num2

def SumListReverse(link1, link2):
    num1 = link1.get_num_reverse()
    num2 = link2.get_num_reverse()
    print(num1, num2)
    return num1 + num2


if __name__ == '__main__':

    link1 = SLinkedList()
    link1.add('1')
    link1.add('5')
    link1.add('2')
    link1.add('4')

    link2 = SLinkedList()
    link2.add('3')
    link2.add('2')
    link2.add('1')

    print(SumList(link1, link2))
    print(SumListReverse(link1, link2))
