from bitstring import Bits, BitArray, BitStream, pack

a = BitArray(bin='00101')

print(a)
print(a.uint)

# b = Bits(uint=7)
b = Bits(uint=28, length=10)
print(b)

print('--------------------------------')
n1 = 13
print(bin(n1).zfill(8))
n1 <<= 1
print(bin(n1).zfill(8))
n1 >>= 2
print(bin(n1).zfill(8))
print('--------------------------------')

n2 = 21
n3 = n1 & n2
print("n1 & n2: ", n3)
print(bin(n1)[2:].zfill(8))
print(bin(n2)[2:].zfill(8))
print(bin(n3)[2:].zfill(8))
print(bin(~n3)[2:].zfill(8))

negnum = -28
print(bin(negnum))

a = 5
