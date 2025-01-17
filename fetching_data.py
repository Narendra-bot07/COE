from connection import cursor
cursor.execute("select * from student")
results = cursor.fetchall()
for x in results:
    print(x)