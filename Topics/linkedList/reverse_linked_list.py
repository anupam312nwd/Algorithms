#!/usr/bin/env python


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseLinkedList_recur(head, prev=None):
    if head.next is None:
        head.next = prev
        return head
    temp = head.next
    head.next = prev
    return reverseLinkedList_recur(temp, head)


def reveseLinkedList_iter(head):
    prev = None
    while head.next:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    head.next = prev
    return head


def printLinkedList(head):
    while head.next:
        print(head.val, end=" -> ")
        head = head.next
    print(head.val)


def getLinkedList():
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(7)
    head.next.next.next = Node(9)
    return head


if __name__ == "__main__":
    head = getLinkedList()
    node = reverseLinkedList_recur(head)
    printLinkedList(node)
    head = getLinkedList()
    node = reveseLinkedList_iter(head)
    printLinkedList(node)
