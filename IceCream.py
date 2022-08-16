import tkinter.messagebox
from asyncio.windows_events import NULL
from tkinter import*
yy=Tk()
yy.title('Restaurant Bot')
yy.iconbitmap('D:\AMR\python project\\New folder\\Restaurant\\Images\\restaurant.ico')
photo=PhotoImage(file='D:\AMR\python project\\New folder\\Restaurant\\Images\\icecream.png')
panel=Label(yy, image=photo)
panel.pack()
width=500
height=450
screenwidth = yy.winfo_screenwidth()
screenheight = yy.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
yy.geometry(f"{width}x{height}+{x}+{y}")
yy.resizable(False,False)
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()
var10 = BooleanVar()
var11 = BooleanVar()
var12 = BooleanVar()
var13 = BooleanVar()
var14 = BooleanVar()
c1=Checkbutton(yy, text='Gummy Bears',variable=var1)
c1.place(x=10,y=20)
l1=Label(yy,text='20 ')
l1.place(x=220,y=20)
sp1=Spinbox(yy,from_=1,to=100,width='10')
sp1.place(x=130,y=20)
c2=Checkbutton(yy, text='Mint Chip',variable=var2)
c2.place(x=10,y=50)
l2=Label(yy,text='20 ')
l2.place(x=220,y=50)
sp2=Spinbox(yy,from_=1,to=100,width='10')
sp2.place(x=130,y=50)
c3=Checkbutton(yy, text='Salted Caramel',variable=var3)
c3.place(x=10,y=80)
l3=Label(yy,text='20 ')
l3.place(x=220,y=80)
sp3=Spinbox(yy,from_=1,to=100,width='10')
sp3.place(x=130,y=80)
c4=Checkbutton(yy, text='Chocolate ',variable=var4)
c4.place(x=10,y=110)
l4=Label(yy,text='20 ')
l4.place(x=220,y=110)
sp4=Spinbox(yy,from_=1,to=100,width='10')
sp4.place(x=130,y=110)
c5=Checkbutton(yy, text='Vanilla Bean',variable=var5)
c5.place(x=10,y=140)
l5=Label(yy,text='20 ')
l5.place(x=220,y=140)
sp5=Spinbox(yy,from_=1,to=100,width='10')
sp5.place(x=130,y=140)
c6=Checkbutton(yy, text='Coffee Oreo ',variable=var6)
c6.place(x=10,y=170)
l6=Label(yy,text='20 ')
l6.place(x=220,y=170)
sp6=Spinbox(yy,from_=1,to=100,width='10')
sp6.place(x=130,y=170)
c7=Checkbutton(yy, text='Reeses Pieces',variable=var7)
c7.place(x=10,y=200)
l7=Label(yy,text='20 ')
l7.place(x=220,y=200)
sp7=Spinbox(yy,from_=1,to=100,width='10')
sp7.place(x=130,y=200)
c8=Checkbutton(yy, text='Peanut Butter',variable=var8)
c8.place(x=10,y=230)
l8=Label(yy,text='20 ')
l8.place(x=220,y=230)
sp8=Spinbox(yy,from_=1,to=100,width='10')
sp8.place(x=130,y=230)
c9=Checkbutton(yy, text='Strawberry',variable=var9)
c9.place(x=10,y=260)
l9=Label(yy,text='20 ')
l9.place(x=220,y=260)
sp9=Spinbox(yy,from_=1,to=100,width='10')
sp9.place(x=130,y=260)
c10=Checkbutton(yy, text='Ocean Water',variable=var10)
c10.place(x=10,y=290)
l10=Label(yy,text='20 ')
l10.place(x=220,y=290)
sp10=Spinbox(yy,from_=1,to=100,width='10')
sp10.place(x=130,y=290)
c11=Checkbutton(yy, text='Passionfruit',variable=var11)
c11.place(x=10,y=320)
l11=Label(yy,text='20 ')
l11.place(x=220,y=320)
sp11=Spinbox(yy,from_=1,to=100,width='10')
sp11.place(x=130,y=320)
c12=Checkbutton(yy, text='Oreos',variable=var12)
c12.place(x=10,y=350)
l12=Label(yy,text='20 ')
l12.place(x=220,y=350)
sp12=Spinbox(yy,from_=1,to=100,width='10')
sp12.place(x=130,y=350)
c13=Checkbutton(yy, text='Sprinkles ',variable=var13)
c13.place(x=10,y=380)
l13=Label(yy,text='20 ')
l13.place(x=220,y=380)
sp13=Spinbox(yy,from_=1,to=100,width='10')
sp13.place(x=130,y=380)
c14=Checkbutton(yy, text='Sea Salt',variable=var14)
c14.place(x=10,y=410)
l14=Label(yy,text='20 ')
l14.place(x=220,y=410)
sp14=Spinbox(yy,from_=1,to=100,width='10')
sp14.place(x=130,y=410)
c1.deselect()
c2.deselect()
c3.deselect()
c4.deselect()
c5.deselect()
c6.deselect()
c7.deselect()
c8.deselect()
c9.deselect()
c10.deselect()
c11.deselect()
c12.deselect()
c13.deselect()
c14.deselect()

def iceCream_order():
    user_order = []
    if var1.get() == True:
        user_order.append(sp1.get() + ' ' + c1['text'] + '    ' + str(int(l1['text']) * int(sp1.get())) + ' EGP')
    if var2.get() == True:
        user_order.append(sp2.get() + ' ' + c2['text'] + '    ' + str(int(l2['text']) * int(sp2.get())) + ' EGP')
    if var3.get():
        user_order.append(sp3.get() + ' ' + c3['text'] + '    ' + str(int(l3['text']) * int(sp3.get())) + ' EGP')
    if var4.get() == True:
        user_order.append(sp4.get() + ' ' + c4['text'] + '    ' + str(int(l4['text']) * int(sp4.get())) + ' EGP')
    if var5.get() == True:
        user_order.append(sp5.get() + ' ' + c5['text'] + '    ' + str(int(l5['text']) * int(sp5.get())) + ' EGP')
    if var6.get() == True:
        user_order.append(sp6.get() + ' ' + c6['text'] + '    ' + str(int(l6['text']) * int(sp6.get())) + ' EGP')
    if var7.get() == True:
        user_order.append(sp7.get() + ' ' + c7['text'] + '    ' + str(int(l7['text']) * int(sp7.get())) + ' EGP')
    if var8.get() == True:
        user_order.append(sp8.get() + ' ' + c8['text'] + '    ' + str(int(l8['text']) * int(sp8.get())) + ' EGP')
    if var9.get() == True:
        user_order.append(sp9.get() + ' ' + c9['text'] + '    ' + str(int(l9['text']) * int(sp9.get())) + ' EGP')
    if var10.get() == True:
        user_order.append(sp10.get() + ' ' + c10['text'] + '    ' + str(int(l10['text']) * int(sp10.get())) + ' EGP')
    if var11.get() == True:
        user_order.append(sp11.get() + ' ' + c11['text'] + '    ' + str(int(l11['text']) * int(sp11.get())) + ' EGP')
    if var12.get() == True:
        user_order.append(sp12.get() + ' ' + c12['text'] + '    ' + str(int(l12['text']) * int(sp12.get())) + ' EGP')
    if var13.get() == True:
        user_order.append(sp13.get() + ' ' + c13['text'] + '    ' + str(int(l13['text']) * int(sp13.get())) + ' EGP')
    if var14.get() == True:
        user_order.append(sp14.get() + ' ' + c14['text'] + '    ' + str(int(l14['text']) * int(sp14.get())) + ' EGP')

    # test code
    final_value = ('\n').join(user_order)

    tkinter.messagebox.showinfo('order', final_value)
    # u just return final_value to get info
def total_price():
    tp = 0

    if var1.get() == True:
        tp += int(l1['text']) * int(sp1.get())
    if var2.get() == True:
        tp += int(l2['text']) * int(sp2.get())
    if var3.get() == True:
        tp += int(l3['text']) * int(sp3.get())
    if var4.get() == True:
        tp += int(l4['text']) * int(sp4.get())
    if var5.get() == True:
        tp += int(l5['text']) * int(sp5.get())
    if var6.get() == True:
        tp += int(l6['text']) * int(sp6.get())
    if var7.get() == True:
        tp += int(l7['text']) * int(sp7.get())
    if var8.get() == True:
        tp += int(l8['text']) * int(sp8.get())
    if var9.get() == True:
        tp += int(l9['text']) * int(sp9.get())
    if var10.get() == True:
        tp += int(l10['text']) * int(sp10.get())
    if var11.get() == True:
        tp += int(l11['text']) * int(sp11.get())
    if var12.get() == True:
        tp += int(l12['text']) * int(sp12.get())
    if var13.get() == True:
        tp += int(l13['text']) * int(sp13.get())
    if var14.get() == True:
        tp += int(l14['text']) * int(sp14.get())

    # test code
    tkinter.messagebox.showinfo('Total price', tp)

def submit():
    yy.destroy()
    import result
def back():
    yy.destroy()
    import f2
bt1=Button(yy,text='Back',font=('courier',15,'bold'),bg='whitesmoke',activebackground='green',command=back)
bt1.place(x=420,y=400)
bt2=Button(yy,text='Submit',font=('courier',15,'bold'),bg='whitesmoke',activebackground='green',command=iceCream_order)
bt2.place(x=320,y=400)
yy.mainloop()
