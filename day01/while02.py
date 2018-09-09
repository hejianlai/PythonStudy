#!/usr/bin/env python
#-*- coding:utf-8 -*-
for i in range(0,10):
    if i <5:
        print("loop",i)
    else:
        break
    print("hehe...")

for i in range(10):
    print('-------------',i)
    for j in range(10):
        print('----------',j)
        if j >5:
            break