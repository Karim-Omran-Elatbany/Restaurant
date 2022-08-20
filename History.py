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
#pro.iconbitmap('D:\AMR\python project\\New folder\\Restaurant\\Images\\restaurant.ico')
def Reset():
    pro.destroy()
    import History
f2=Frame(pro,bd=2,width=500,height=100,bg='#0B4C5F')
f2.place(x=1,y=400)
bt1=Button(f2,text='Reset',font=('courier',15,"bold"),bg='black',fg='white',width=7,height=1,command=Reset)
bt1.place(x=50,y=30)
def Exit():
    pro.destroy()
    import HomeScreen
bt2=Button(f2,text='Exit',font=('courier',15,"bold"),bg='black',fg='white',width=7,height=1,command=Exit)
bt2.place(x=200,y=30)
bt3=Button(f2,text='Show',font=('courier',15,"bold"),bg='black',fg='white',width=7,height=1)
bt3.place(x=350,y=30)
columns=['order','Best Seller']
tree=Treeview(pro,columns=columns,show='headings',height=19)
scroll=Scrollbar(pro,orient=VERTICAL,command=tree.yview)
scroll.grid(row=0,column=1,sticky='ns')
tree.configure(yscroll=scroll.set)
tree.column('order',width=240,anchor='center')

tree.column('Best Seller',width=240,anchor='center')

tree.heading('order',text='order')

tree.heading('Best Seller',text='Best Seller')

tree.grid(column=0,row=0)
pro.mainloop()
