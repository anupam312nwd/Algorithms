import numpy as np

a = np.random.rand(2, 3)
b = np.random.randn(2, 3)
k = np.random.randint(0, 9, (4, 5))

c = {"name": "AK", "class": "PhD", "major": "maths"}
for t in c:
    print(t, c[t])


print(a)
print(b)
print(k)
