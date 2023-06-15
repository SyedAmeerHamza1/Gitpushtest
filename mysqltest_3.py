# selecting particular columns only

import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Sohail_123")
cursor = mydb.cursor()

cursor.execute("select employee_id, employee_salary,  employee_name  from sohail.table1")

for i in cursor.fetchall():
    print(i)