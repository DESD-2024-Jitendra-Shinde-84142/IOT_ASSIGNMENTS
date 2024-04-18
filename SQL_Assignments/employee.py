import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

query1 = "select * from Employee;"
query3 = "select * from Employee order by salary DESC LIMIT 1;"
query4 = "select * from Employee order by salary ASC LIMIT 1;"

cursor = connection.cursor()

cursor.execute(query1)

records = cursor.fetchall()    

print("")
for ele in records:
    print(ele)

print("")
department = input("Enter department : ")
query2 = f"select * from Employee where department = %s;"
val = (department, )

cursor.execute(query2, val)

records = cursor.fetchall()    

print("")
for ele in records:
    print(ele)

cursor.execute(query3)

records = cursor.fetchall()    

print("")
for ele in records:
    print(ele)

cursor.execute(query4)

records = cursor.fetchall()    

print("")
for ele in records:
    print(ele)

cursor.close()

connection.close()