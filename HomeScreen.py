from tkinter import*
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
#pro.iconbitmap('E:\\restaurant\\restaurant.ico') 
#photo=PhotoImage(file='E:\\restaurant\\HomeScreen.png')
#panel=Label(pro, image=photo)
#panel.pack()
def manager():
    pro.destroy()
    import History
bt1=Button(pro,text='Manager',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=manager)
bt1.place(x=60,y=250)
def User():
    pro.destroy()
    import Home
bt2=Button(pro,text='User',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=User)
bt2.place(x=300,y=250)


pro.mainloop()