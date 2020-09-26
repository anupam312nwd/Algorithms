""" implement a data structure SetOfStacks that behaves as a stack and start a new stack once
    the previous one exceeds capacity.
"""

class SetOfStack(list):
    def __init__(self, limit=4):
        self.limit = limit

    def append(self, object):
        if not self:
            super().append([])
            self[0].append(object)
        else:
            if len(self[-1]) < self.limit:
                self[-1].append(object)
            else:
                self.append([])
                self[-1].append(object)

lst = SetOfStack()
lst.append(7)
lst.append(6)
lst.append(7)
print(lst)
lst.append(7)
lst.append(8)
lst.append(1)
lst.append(3)
print(lst)
