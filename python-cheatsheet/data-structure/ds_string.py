#!/usr/bin/env python

for i in range(ord('a'), ord('z') + 1):
    print(chr(i))

mapping = {chr(i): ord(chr(i)) - ord('a') for i in range(ord('a'), ord('z') + 1)}
print(mapping)
