from connection import mydb,cursor
id = int(input("Enter id to delete "))
query = "delete from student where id=%s"
values = ([id])
cursor.execute(query,values)
mydb.commit()
