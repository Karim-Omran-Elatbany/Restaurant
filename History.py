from tkinter import*
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
def Reset():
    pro.destroy()
    import History
f2=Frame(pro,bd=2,width=500,height=100,bg='#0B4C5F')
f2.place(x=1,y=400)
bt1=Button(f2,text='Reset',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=Reset)
bt1.place(x=50,y=30)
f3=Frame(pro,bd=2,width=500,height=60,bg='white')
f3.place(x=1,y=340)
l1 = Label(f3,text='Price:',font=('courier',15,'bold'),bg='black',fg='white')
l1.place(x=10,y=20)
l2 = Label(f3,text='Number:',font=('courier',15,'bold'),bg='black',fg='white')
l2.place(x=250,y=20)
def Exit():
    pro.destroy()
    import HomeScreen
bt2=Button(f2,text='Exit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=Exit)
bt2.place(x=300,y=30)
columns=['id','name','order','salary']
tree=Treeview(pro,columns=columns,show='headings',height=16)
scrol=Scrollbar(pro,orient=VERTICAL,command=tree.yview)
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
