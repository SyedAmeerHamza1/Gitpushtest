# Trying to push files to git


import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Sohail_123")
cursor = mydb.cursor()
print(mydb)

# converting into comments because code has already executed
#s = "create table sohail.table1(employee_id int(10), employee_name varchar(20), employee_mailid varchar(20), " \
    # "employee_salary int(6), employee_attendance int(3))"

# q1=cursor.execute(s)

q2 = cursor.execute("select * from sohail.table1")



