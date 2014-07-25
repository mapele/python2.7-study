

import sqlite3 
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#cursor.execute('insert into user (id, name) values (\'4\', \'Michael\')')
#conn.commit
#print(cursor.rowcount)

cursor.execute('select count(*) from user')
values = cursor.fetchall()
print(values)

cursor.execute('select * from user')
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
