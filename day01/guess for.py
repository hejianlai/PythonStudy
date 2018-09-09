#!/usr/bin/env python
#-*- coding:utf-8 -*-
age_of_oldboy = 23
for i in range(3):
    gues_age = int(input("guess age:"))
    if gues_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif gues_age > age_of_oldboy:
        print("think smaller..")
    else:
        print("think bigger")
