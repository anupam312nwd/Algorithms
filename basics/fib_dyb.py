#!/usr/bin/env python

fb_cache = {}

def fib(n):
    return fb_c(n-1) + fb_c(n-2)

def fb_c(i):
    if (i==0 or i==1):
        fb_cache[i] = i
        return fb_cache[i]
    else:
        if i in fb_cache.keys():
            fb_cache[i] = fb_cache[i-1] + fb_cache[i-2]
        else:
            fb_cache[i] = fb_c(i-1) + fb_c(i-2)
        return fb_cache[i]

print(fib(55))
