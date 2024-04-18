import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_employee(empid, salary):
    conn = get_connection()

    query = f"update Employee SET salary = %s where empid = %s;"
    val = (salary, empid)

    cursor = conn.cursor()

  
    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()

update_employee(1004, 35000)













