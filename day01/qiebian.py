#!/usr/bin/env python
#-*- coding:utf-8 -*-
L = []
n = 1
while n < 99:
    L.append(n)
    n = n + 2
for i in L:
    print(i)

print(L[0:10:2])