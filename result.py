from cgitb import text
from sys import flags
from tkinter import*
import tkinter.messagebox
from tkinter.ttk import Treeview
pro=Tk()
pro.title('Restaurant Bot')
width=500
height=500
screenwidth = pro.winfo_screenwidth()
screenheight = pro.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
pro.geometry(f"{width}x{height}+{x}+{y}")
pro.resizable(False,False)
pro.iconbitmap('D:\AMR\python project\\New folder\\Restaurant\\Images\\restaurant.ico')
l1=Label(pro,text='الفاتورة',font=('courier',15,"bold"),bg='black',fg='white')
l1.pack(fill=X)
f1=Frame(pro,bd=2,bg='white')
f1.place(x=0,y=0)
f2=Frame(pro,bd=2,width=500,height=110,bg='#0B4C5F')
f2.place(x=1,y=390)
def submit():
        tkinter.messagebox.showinfo('System','Thanks')
        pro.destroy()
        import HomeScreen
def exit():
    pro.destroy()
    import  HomeScreen
bt1=Button(f2,text='Submit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=submit)
bt1.place(x=10,y=30)
bt3=Button(f2,text='Edit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1)
bt3.place(x=180,y=30)
bt2=Button(f2,text='Exit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=exit)
bt2.place(x=350,y=30)
columns=['id','name','order','salary']
tree=Treeview(f1,columns=columns,show='headings',height=18)
scrol=Scrollbar(f1,orient=VERTICAL,command=tree.yview)
scrol.grid(row=0,column=1,sticky='ns')
tree.column('id',width=80,anchor='center')
tree.column('name',width=100,anchor='center')
tree.column('order',width=200,anchor='center')
tree.column('salary',width=100,anchor='center')
tree.heading('id',text='id')
tree.heading('name',text='name')
tree.heading('order',text='order')
tree.heading('salary',text='salary')
tree.grid(column=0,row=0)
pro.mainloop()
