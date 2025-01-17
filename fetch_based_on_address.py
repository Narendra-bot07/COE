from connection import cursor
address = input("Enter address (hyderabad or andhra): ")
cursor.execute("select * from student where address=%s",([address]))
result = cursor.fetchall()
for x in result:
    print(x)