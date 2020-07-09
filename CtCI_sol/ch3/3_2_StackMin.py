""" design Stack which along w pop() and posh(), also returns minimum element in O(1) time """
""" maintain another stack (call it min-stack) whose top elem is the min elem by:
    1. if elem pushed to main stack is less than equal to elem of min-stack, then push that elem to min-stack
    2. if elem popped is same as top elem of min-stack, pop that elem from min-stack too
    - min-stack.peek() is the min elem of main stack """


class stack(list):

    def __init__(self, minstack=None):
        self.minstack = []

    def append(self, obj):
        if self.minstack:
            if self.minstack[-1] >= obj:
                # print("peek elem", self[-1])
                self.minstack.append(obj)
        else:
            self.minstack.append(obj)
        return super(stack, self).append(obj)

    def pop(self):
        if list:
            if self.minstack[-1] == self[-1]:
                self.minstack.pop()
        return super(stack, self).pop()

    def call_min(self):
        return self.minstack[-1]


if __name__ == '__main__':

    lst = stack()
    lst.append(3)
    lst.append(4)
    lst.append(2)
    lst.append(7)
    lst.append(8)
    lst.pop()
    lst.pop()
    lst.pop()
    lst.pop()
    lst.append(5)
    print(lst)
    print(lst.call_min())
    print(lst.minstack)
    lst.append(1)
    lst.append(1)
    lst.append(1)
    lst.append(6)
    lst.append(8)

    print(lst)
    print(lst.call_min())
    print(lst.minstack[-1])
