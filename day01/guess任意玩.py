#!/usr/bin/env python
#-*- coding:utf-8 -*-
age_of_oldboy = 23
count = 0
while count <3:
    gues_age = int(input("guess age:"))
    if gues_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif gues_age > age_of_oldboy:
        print("think smaller..")
    else:
        print("think bigger")
    count +=1
    if count == 3:
        countine_game = input("do you want to keep guessing..?")
        if countine_game != 'n':
            count = 0
