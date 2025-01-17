from connection import cursor
cursor.execute("select * from student where score>70 and score<90")
result = cursor.fetchall()
for x in result:
    print(x)