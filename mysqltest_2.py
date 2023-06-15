import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Sohail_123")
cursor = mydb.cursor()
s = "insert into sohail.table1 values(100,'SohailHamza', 'Sohail@gmail.com', 100, 30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
mydb.commit()

cursor.execute('select * from sohail.table1')

var = [i for i in cursor.fetchall()]

print(var)
