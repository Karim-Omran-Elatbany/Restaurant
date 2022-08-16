from ctypes import sizeof
from ctypes.wintypes import RGB
from email.mime import image
from msilib.schema import Icon
from tkinter import*
from typing import Sized
tt=Tk()
tt.title('Restaurant Bot')
tt.iconbitmap('D:\AMR\python project\\New folder\\Restaurant\\Images\\restaurant.ico')
width=500
height=500
screenwidth = tt.winfo_screenwidth()
screenheight = tt.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
tt.geometry(f"{width}x{height}+{x}+{y}")
tt.resizable(False,False)
fr2=Frame(tt)
fr2.pack(pady=30)
img=PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\fff.png')
label = Label(
    tt,
    image=img
)
label.place(x=0,y=0)
photo1 = PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\coffee.png')
photo2 = PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\drinks.png')
photo3 = PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\gujrati-food.png')
photo4 = PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\ice-cream.png')
def IceCream():
    tt.destroy()
    import IceCream
def coffee():
    tt.destroy()
    import coffee
def Soda():
    tt.destroy()
    import Soda
def food():
    tt.destroy()
    import Food
bt1=Button(
    tt,
     text = 'Coffee',
     font=('#7DE1D5',15,"bold"),
      image = photo1,
      compound ='left',
      height='50',
      width='150',
      border= '0',
      activebackground='#363638',
      command=coffee
      )
bt1.place(x=20,y=150)
bt2=Button(
    tt,
     text = 'Soda',
     font=('#7DE1D5',15,"bold"),
      image = photo2,
      compound ='lef',
      height='50',
      width='150',
      border='0',
      activebackground='#363638',
      command=Soda
      )
bt2.place(x=20,y=250)
bt4=Button(tt, text = 'Ice Cream',font=('#7DE1D5',12,"bold"), 
image = photo4,
compound ='left',height='50',width='150',border='0',activebackground='#363638',command=IceCream)
bt4.place(x=320,y=150)
bt3=Button(tt, text = 'Food',font=('#7DE1D5',15,"bold"),
 image = photo3,
 compound ='left',height='50',width='150',border='0',activebackground='#363638',command=food)
bt3.place(x=320,y=250)
tt.mainloop()
