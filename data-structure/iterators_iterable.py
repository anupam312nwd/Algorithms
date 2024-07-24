class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end):
    current = start
    while True:
        yield current
        current += 1
        if current >= end:
            break


def iterable_to_iterator():
    nums = [1, 2, 3]
    i_nums = iter(nums)
    print(dir(nums))
    print(f'i_nums: {i_nums}')
    print(dir(i_nums))


if __name__ == '__main__':

    iterable_to_iterator()
    nums = MyRange(1, 4)
    for num in nums:
        print(num)

    print('-----------------------')

    nums = my_range(1, 5)
    for num in nums:
        print(num)
