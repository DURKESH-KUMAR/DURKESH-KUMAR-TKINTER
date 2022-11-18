import sqlite3

class Database:
    def __init__(self,db):
        self.connection=sqlite3.connect(db)
        self.cursor=self.connection.cursor()
        x="""
        create table if not exists employees(
            id INTEGER NOT NULL,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cursor.execute(x)
        self.connection.commit()
    
    #insert command
    def insert(self,id,name,age,doj,email,gender,contact,address):
        x="""insert into employees(id,name,age,doj,email,gender,contact,address) values ("{}","{}","{}","{}","{}","{}","{}","{}") """.format(id,name,age,doj,email,gender,contact,address)
        self.cursor.execute(x)
        self.connection.commit()
    #display the records
    def fetch(self):
        self.cursor.execute("select *from employees")
        x=self.cursor.fetchall()
        return x
    
    #delete a record in db 
    def remove(self,id):
        self.cursor.execute("""delete from employees where id="{}" """.format(id))
        self.connection.commit()
    
    #update a record in db
    def update(self,id,name,age,doj,email,gender,contact,address):
        x="""update employees set name="{}",age="{}",doj="{}",email="{}",gender="{}",contact="{}",address="{}" where id="{}" """.format(name,age,doj,email,gender,contact,address,id)
        self.cursor.execute(x)
        self.connection.commit()

o=Database("employees.db")
