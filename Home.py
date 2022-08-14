from sys import flags
from tkinter import*
import tkinter.messagebox
from tkinter.font import BOLD
from urllib.parse import urldefrag
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
pro.config(background='#D5DBDB')
#pro.iconbitmap('E:\\restaurant\\restaurant.ico') 
title = Label(pro,text='Welcome',font=('courier',15,"bold"),bg='black',fg='white')
title.pack(fill=X)
fr1=Frame(pro,width=300,height=350,bg='whitesmoke')
fr1.pack(pady=30)
def home():
    flag=False
   
    user_name=ent_username.get()#if u didn't enter username the value will be ""
    length=len(user_name)
    if user_name!="" and length>=3:
        flag=True
        
    if flag==False:
        tkinter.messagebox.showerror('System','Please enter user name')
    if flag==True:
        pro.destroy()
        import f2
        
#photo=PhotoImage(file='E:\\restaurant\\restaurant.png')
#panel=Label(fr1, image=photo)
#panel.place(x=100,y=30)
l1 = Label(fr1,text='Username:',font=('courier',15,'bold'))
l1.place(x=10,y=140)
ent_username=Entry(fr1,justify='center')
ent_username.place(x=130,y=145)
bt1=Button(fr1,text='Submit',font=('courier',15,'bold'),bg='whitesmoke',activebackground='green',command=home)
bt1.place(x=100,y=200)
pro.mainloop()
