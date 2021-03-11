#!/usr/bin/env python3
"""Let's write a function falling, which is a "falling" factorial that takes two arguments, n and k, and returns the product of k consecutive numbers, starting from n and working downwards. When k is 0, the function should return 1."""

def falling(n,k):
    if(k==0):
        return 1
    else:
        return n*falling(n-1,k-1)

n=input()
k = input()
print(falling(int(n),int(k)))
