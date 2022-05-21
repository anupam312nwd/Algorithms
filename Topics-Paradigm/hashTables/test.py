dict = {"ak": 5, "ad": 7, "ag": 6}
print(dict.keys)
print(dict.keys())
print(dict.get("ak"), dict["ak"])

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

a = Node('b')
print(a)
print(a.data)
print(a.next)
print(a.data=='b')
