from tkinter import *
#importing tkinter modules as ttk 
from tkinter import ttk
#importing database
from db import Database
#database name
db=Database("employees.db")
#code to show the message box
from tkinter import messagebox

#gendral setup  for tkinter 

root=Tk()
root.title("durkesh kumar management system")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")
#string
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#entries frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="employee management system",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)
#name
lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=20,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=20,sticky="w")
#age
lblage=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=20,sticky="w")
txtage=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtage.grid(row=1,column=3,padx=10,pady=20,sticky="w")
#date of join
lbldoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=20,sticky="w")
txtdoj=Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=20,sticky="w")
#gender
lblgender=Label(entries_frame,text="GENDER",font=("Calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=2,column=2,padx=10,pady=20,sticky="w")
txtgender=Entry(entries_frame,textvariable=gender,font=("Calibri",16),width=30)
txtgender.grid(row=2,column=3,padx=10,pady=20,sticky="w")
#email
lblemail=Label(entries_frame,text="EMAIL",font=("Calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=3,column=0,padx=10,pady=20,sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtemail.grid(row=3,column=1,padx=10,pady=20,sticky="w")
#contact
lblcontact=Label(entries_frame,text="CONTACT",font=("Calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=20,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=20,sticky="w")

#address
lbladdress=Label(entries_frame,text="ADDRESS",font=("Calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtaddress=Text(entries_frame,width=85,height=5,font=("Calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

#button
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row 
    row=data["values"]
    # print(row) used to check 
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    email.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])
    
def displayall():
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or txtgender.get()=="" or txtcontact.get()=="":
        messagebox.showerror("error in input"," one of the input was not filled")
        return 
    db.insert(txtName.get,txtage.get(),txtdoj.get(),txtemail.get(),txtgender.get(),txtcontact.get())
    messagebox("success","record inserted")
    clearall()
    displayall()


def update_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or txtgender.get()=="" or txtcontact.get()=="":
        messagebox.showerror("error in input"," one of the input was not filled")
        return 
    db.update(row[0],txtName.get,txtage.get(),txtdoj.get(),txtemail.get(),txtgender.get(),txtcontact.get())
    messagebox("success","record updated")
    clearall()
    displayall()
    
def delete_employee():
    db.remove(row[0])
    clearall()
    displayall()
def clearall():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)
btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
#add users
btnadd=Button(btn_frame,command=add_employee,text="add details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#16a885").grid(row=0,column=0,padx=10)
#update users
btnedit=Button(btn_frame,command=update_employee,text="update details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#16a885").grid(row=0,column=1,padx=10)
#delete users
btndelete=Button(btn_frame,command=delete_employee,text="delete details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#16a885").grid(row=0,column=2,padx=10)
#clear all
btnclear=Button(btn_frame,command=clearall,text="clear details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#16a885").grid(row=0,column=3,padx=10)

#down side facing 
tree_frame=Frame(root,bg="#ecf8f1")
tree_frame.place(x=0,y=540,width=1980,height=520)

#ttk tree view
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",18),rowheight=50)#modify the font of thr body 
style.configure("mystyle.Treeview.Heading",font=("Calibri",18))#modify the font of the heading 
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=2)
tv.heading("2",text="NAME")
tv.column("2",width=5)
tv.heading("3",text="AGE")
tv.column("3",width=5)
tv.heading("4",text="D.O.B")
tv.column("4",width=5)
tv.heading("5",text="EMAIL")
tv.column("5",width=5)
tv.heading("6",text="GENDER")
tv.column("6",width=5)
tv.heading("7",text="CONTACT")
tv.column("7",width=5)
tv.heading("8",text="ADDRESS")

tv["show"]="headings"
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayall()



#table frame
root.mainloop()