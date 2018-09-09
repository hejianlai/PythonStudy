#!/usr/bin/env python
#-*- coding:utf-8 -*-
import mysql.connector
conn = mysql.connector.connect(user='root',password='123',database='cmdb')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['2','hejianlailll'])
conn.commit()
cursor.close()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
cursor.close()
conn.close()
