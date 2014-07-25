#!/usr/bin/python  
#-*-coding:utf-8-*-

import mysql.connector

conn = mysql.connector.connect(user='xwy', password='594120', database='test', use_unicode=True)
cursor = conn.cursor()

#创建user表
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#插入数据
cursor.execute('insert into user (id,name) values(%s,%s)', ['5', 'zhangx'])
cursor.rowcount
conn.commit()

#查询
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()