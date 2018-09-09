#!/usr/bin/env python
#-*- coding:utf-8 -*-
def input_num(x):
    if not isinstance(x,(int,float)):
        raise TypeError("type error")
    if x > 0:
        print("true")
    else:
        print("false")
input_num(2)
def nop():
    pass


def power(x,n):
    s = 1
    while n > 0:
        n -=1
        s = s * x
    return s
print(power(2,3))

