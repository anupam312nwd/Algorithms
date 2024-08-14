num = 237
A = map(int, str(num))

for i, x in enumerate(A):
    print(i, x)

print('---------------------')
for i, x in enumerate(str(num)):
    print(i, x)
