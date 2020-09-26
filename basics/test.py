import math

max_num = math.pow(2, 31)
print(max_num - 1 < 1534236469)

a = "anup kumar"
print(a[::-1])
print("".join(reversed(a)))
print(str(725))
a = [7, 2, 3, 1]
b = ["Anup", "rahul", "sumit"]


def reverseBits(n: int) -> int:
    int_to_str = str(n)
    rev_int = "".join(reversed(int_to_str))
    return int(rev_int)


print(reverseBits(91127))
print(reverseBits(720407136))

n = 3
bin_n = bin(n)[2:].rjust(4, "0")
print(bin_n)
print(pow(2, 4))
