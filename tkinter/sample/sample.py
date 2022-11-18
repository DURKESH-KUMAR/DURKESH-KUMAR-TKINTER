import sqlite3
connection=sqlite3.connect("employees.db")
cursor=connection.cursor()
# x="""insert into employees (id,name,age,doj,email,gender,contact,address) values(1,"durkesh",15,"12-11-2022","durkesh@gmail.com","male","6374912478","chennai")"""
# cursor.execute(x)
# connection.commit()
cursor.execute("select *from employees")
x=cursor.fetchall()
print(x)