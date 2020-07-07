import numpy as np

stra = 'Mr John Sm'
strb = stra.replace(" ", "%20")
# print(strb)
# print(stra[:7])

# stra = stra.replace(" ", "")
# print(stra)

# if stra: print("True")
print(list(stra))
stra = "taco"
strb = "tabo"

print(list(stra) == list(strb))
# print(np.array(list(stra)) == np.array(list(strb)))
tf_list = np.array(list(stra)) == np.array(list(strb))
print(tf_list)
print(np.sum(tf_list))
