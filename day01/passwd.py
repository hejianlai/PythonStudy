#!/usr/bin/env python
#-*- coding:utf-8 -*-
import getpass
_username = 'root'
_password = '123'
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")
#print(username,password)