from asyncio.windows_events import NULL
import tkinter.messagebox

from tkinter import *
yy = Tk()
yy.title('Restaurant Bot')
#yy.iconbitmap('D:\AMR\python project\\New folder\\Restaurant\\Images\\restaurant.ico')
#photo = PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\coffeee.png')
#panel = Label(yy, image=photo)
#panel.pack()
width = 500
height = 450
screenwidth = yy.winfo_screenwidth()
screenheight = yy.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
yy.geometry(f"{width}x{height}+{x}+{y}")
yy.resizable(False, False)

var1_For_Tables = BooleanVar()
var2_For_Tables = BooleanVar()
var3_For_Tables = BooleanVar()
var4_For_Tables = BooleanVar()
var5_For_Tables = BooleanVar()
var6_For_Tables = BooleanVar()

#--------this
# photo=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# panel = Label(yy, image=photo)
# panel.place(x=10,y=50)

Table1 = Checkbutton(yy, text=' Single ', variable=var1_For_Tables)
Table1.deselect()
Table1.place(x=10, y=170)

# photo2=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# pane2 = Label(yy, image=photo)
# pane2.place(x=190,y=50)

Table2 = Checkbutton(yy, text=' couple ', variable=var2_For_Tables)
Table2.deselect()
Table2.place(x=190, y=170)

# photo3=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# pane3 = Label(yy, image=photo)
# pane3.place(x=370,y=50)

Table3 = Checkbutton(yy, text=' 4 Friends ', variable=var3_For_Tables)
Table3.deselect()
Table3.place(x=370, y=170)

# photo4=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# pane4 = Label(yy, image=photo)
# pane4.place(x=10,y=250)

Table4 = Checkbutton(yy, text='Family ', variable=var4_For_Tables)
Table4.deselect()
Table4.place(x=10, y=360)

# photo5=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# pane5 = Label(yy, image=photo)
# pane5.place(x=190,y=250)

Table5 = Checkbutton(yy, text='6 Friends', variable=var5_For_Tables)
Table5.deselect()
Table5.place(x=190, y=360)

# photo6=PhotoImage(file='E:\\Restaurant-main\\Images\\k.png')
# pane6 = Label(yy, image=photo)
# pane6.place(x=370,y=250)

Table6 = Checkbutton(yy, text='8 friends', variable=var6_For_Tables)
Table6.deselect()
Table6.place(x=370, y=360)


#-------Bottom---------
def submit():
    if var2_For_Tables.get():
        tkinter.messagebox.showerror('System', 'Table 2 is already reserved ')
    elif var4_For_Tables.get():
        tkinter.messagebox.showerror('System', 'Table 4 is already reserved ')
    else:
        yy.destroy()
        import main_project


def back():
    yy.destroy()
    import f2


bt1 = Button(yy, text='Back', font=('courier', 15, 'bold'),bg='whitesmoke', activebackground='green', command=back)
bt1.place(x=420, y=400)
bt2 = Button(yy, text='Submit', font=('courier', 15, 'bold'),bg='whitesmoke', activebackground='green', command=submit)
bt2.place(x=320, y=400)

yy.mainloop()
