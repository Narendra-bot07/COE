from connection import cursor,mydb
id=int(input("Enter id of a student: "))
address = (input("Enter address of a student: "))
cursor.execute("update student set address=%s where id=%s",([address,id]))
mydb.commit()