from connection import cursor
cursor.execute("select * from student order by name asc")
result = cursor.fetchall()
print(result)
for x in result:
    print(x[0]," ",x[1])
