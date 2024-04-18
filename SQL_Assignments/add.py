import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter department : ")
email = input("Enter email :")
salary = input("Enter salary : ")
DOJ = input("Enter DOJ : ")

query = f"insert into Employee values({empid}, '{name}', '{department}', '{email}', '{salary}', '{DOJ}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()