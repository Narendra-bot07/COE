from connection import cursor
id = int(input("Enter the id: "))
name = input("Enter your name: ")
query = "insert into student values(%s,%s)"
values = (id,name)
i = cursor.execute(query,values)
mydb.commit()