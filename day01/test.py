#!/usr/bin/env python
#-*- coding:utf-8 -*-
age_for_my = 23
count = 0
for i in range(3):
    age = int(input("please input you age:"))
    if age_for_my == age:
        print("you true;")
        break
    elif age_for_my > age:
        print("think small!")
    else:
        print("think bigeer!")

