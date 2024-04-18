import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def delete_employee(empid):
    conn = get_connection()

    query = f"delete from Employee where empid = %s;"
    val = (empid, )

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()

delete_employee(1006)













