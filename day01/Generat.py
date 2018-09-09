#!/usr/bin/env python
#-*- coding:utf-8 -*-
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(next(g))
print(next(g))
for i in g:
    print(i)

def add(x,y,f):
    return f(x) + f(y)
print(add(-2,-43,abs))

def f(x):
    return x * x
r = map(f,[1,2,3,4,5])
print(list(r))

def is_old(n):
    return n % 2 ==1
list(filter(is_old[1,23,4,5,23,5,67,3]))