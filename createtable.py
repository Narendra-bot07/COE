from connection import cursor,mydb
insert_query = "insert into customers values(%s,%s,%s)"
values = (1,'narendra','andhra')
cursor.execute(insert_query,values)
mydb.commit()