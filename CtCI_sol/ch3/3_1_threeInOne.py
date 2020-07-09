## INCOMPLETE + copied solution
""" use a single array to implement three stacks """


class ThreeStacks():
  def __init__(self):
    self.array = [None, None, None]
    self.current = [0, 1, 2]

  def push(self, item, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    while len(self.array) <= self.current[stack_number]:
      self.array += [None] * len(self.array)
    self.array[self.current[stack_number]] = item
    self.current[stack_number] += 3

  def pop(self, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    if self.current[stack_number] > 3:
      self.current[stack_number] -= 3
    item = self.array[self.current[stack_number]]
    self.array[self.current[stack_number]] = None
    return item


three_stacks = ThreeStacks()

# three_stacks.push(101, 0)
# three_stacks.push(102, 0)
three_stacks.push(3, 0)
three_stacks.push(3, 0)
three_stacks.push(3, 0)
three_stacks.push(3, 0)
three_stacks.push(3, 0)
three_stacks.push(3, 0)
three_stacks.push(4, 1)
print(three_stacks)
print(three_stacks.array)
print(three_stacks.current)
"""
<__main__.ThreeStacks object at 0x7fe092068e50>
[101, 201, None, 102, None, None, 103, None, None, None, None, None]
[9, 4, 2]
"""
three_stacks.push(7, 2)
print(three_stacks.array)
print(three_stacks.current)

three_stacks.push(5, 1)
three_stacks.push(5, 1)
three_stacks.push(5, 1)
three_stacks.push(7, 2)
three_stacks.push(7, 2)
three_stacks.push(7, 2)
three_stacks.push(5, 1)
three_stacks.push(5, 1)
three_stacks.push(5, 1)
print(three_stacks.array)
print(three_stacks.current)
