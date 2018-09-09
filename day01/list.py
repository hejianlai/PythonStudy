#!/usr/bin/env python
#-*- coding:utf-8 -*-
name = ['hejianlai','root']
print(name[0],name[1])
name.append('add')
print(name)
name.insert(1,'hehe')
print(name)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("HELLO:",i)

print(L.sort())


print(abs(-233))
num = 23
print(hex(num))
print(str(num))
