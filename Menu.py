from distutils.cmd import Command
from distutils.command.config import config
from tkinter import*
import math ,random,os
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD
from tkinter.ttk import Treeview
# center the main window according to screen
class Restaurant:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x600+30+10")
        self.root.title('Restaurant Bot')
        self.root.resizable(False,False)
        #self.root.iconbitmap('E:\\Restaurant-main\\Images\\restaurant.ico')
        title = Label(root,text='Restaurant Menu',fg='white',bg='#0B2F3A',font=('tomato',15))
        title.pack(fill=X)
        F1=Frame(self.root,bd=2, width=338,height=170,bg='#0B4C5F' )
        F1.place(x=961,y=30)
        t = Label(F1,text='Search For Customer',font=('tomato',15,BOLD),bg='#0B4C5F',fg='gold')
        t.place(x=75,y=0)

        #----------------------Search-----------------
        his_name =Label( F1 , text='Username',font=('tomato',10,BOLD),bg='#0B4C5F',fg='white')
        his_name.place(x=0,y=75)

        Ent_name=Entry(F1)
        Ent_name.place(x=80,y=77)

        btn_Customer = Button(F1,text='Search',font=('tomato',10,BOLD),bg='#0B4C5F',fg='white',width=10,height=3)
        btn_Customer.place(x=230,y=60)

        #---------Result--------------
        Result=Label(F1,text='Restaurant Bot',font=('tomato',13,BOLD),bg='#0B4C5F',fg='gold')
        Result.place(x=110,y=135)
        F2=Frame(root,bd=2, width=338,height=500,bg='white' )
        F2.place(x=962,y=205)
        #------------Output from User----------
        columns=['id','name','order','salary']
        tree=Treeview(F2,columns=columns,show='headings',height=18)
        scroll=Scrollbar(F2,orient=VERTICAL,command=tree.yview)
        scroll.grid(row=0,column=1,sticky='ns')
        tree.column('id',width=50,anchor='center')
        tree.column('name',width=80,anchor='center')
        tree.column('order',width=105,anchor='center')
        tree.column('salary',width=80,anchor='center')
        tree.heading('id',text='id')
        tree.heading('name',text='name')
        tree.heading('order',text='order')
        tree.heading('salary',text='salary')
        tree.grid(column=0,row=0)

        #------------BUttons------------------------------------------
        F3 =Frame(self.root,bd=2, width=958,height=100,bg='#0B4C5F' )
        F3.place(x=1,y=500)

        Exit = Button(F3,text='Exit',font=('tomato',10,BOLD),bg='#0B4C5F',fg='white',width=15,height=2)
        Exit.place(x=600,y=20)


        #------------------------IceCream--------------------------------
        FF1 = Frame(root,bd=2,width=318,height=470,bg='#0B4C5F')
        FF1.place(x=1,y=30)
        t = Label(FF1,text='IceCream',font=('tomato',15,BOLD),bg='#0B4C5F',fg='gold')
        t.place(x=120,y=0)
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
        c1=Checkbutton(FF1, text='Gummy Bears',variable=var1)
        c1.place(x=10,y=30)
        l1=Label(FF1,text='20 ')
        l1.place(x=220,y=30)
        sp1=Spinbox(FF1,from_=1,to=100,width='10')
        sp1.place(x=130,y=30)
        c2=Checkbutton(FF1, text='Mint Chip',variable=var2)
        c2.place(x=10,y=60)
        l2=Label(FF1,text='20 ')
        l2.place(x=220,y=60)
        sp2=Spinbox(FF1,from_=1,to=100,width='10')
        sp2.place(x=130,y=60)
        c3=Checkbutton(FF1, text='Salted Caramel',variable=var3)
        c3.place(x=10,y=90)
        l3=Label(FF1,text='20 ')
        l3.place(x=220,y=90)
        sp3=Spinbox(FF1,from_=1,to=100,width='10')
        sp3.place(x=130,y=90)
        c4=Checkbutton(FF1, text='Chocolate ',variable=var4)
        c4.place(x=10,y=120)
        l4=Label(FF1,text='20 ')
        l4.place(x=220,y=120)
        sp4=Spinbox(FF1,from_=1,to=100,width='10')
        sp4.place(x=130,y=120)
        c5=Checkbutton(FF1, text='Vanilla Bean',variable=var5)
        c5.place(x=10,y=150)
        l5=Label(FF1,text='20 ')
        l5.place(x=220,y=150)
        sp5=Spinbox(FF1,from_=1,to=100,width='10')
        sp5.place(x=130,y=150)
        c6=Checkbutton(FF1, text='Coffee Oreo ',variable=var6)
        c6.place(x=10,y=180)
        l6=Label(FF1,text='20 ')
        l6.place(x=220,y=180)
        sp6=Spinbox(FF1,from_=1,to=100,width='10')
        sp6.place(x=130,y=180)
        c7=Checkbutton(FF1, text='Reeses Pieces',variable=var7)
        c7.place(x=10,y=210)
        l7=Label(FF1,text='20 ')
        l7.place(x=220,y=210)
        sp7=Spinbox(FF1,from_=1,to=100,width='10')
        sp7.place(x=130,y=210)
        c8=Checkbutton(FF1, text='Peanut Butter',variable=var8)
        c8.place(x=10,y=240)
        l8=Label(FF1,text='20 ')
        l8.place(x=220,y=240)
        sp8=Spinbox(FF1,from_=1,to=100,width='10')
        sp8.place(x=130,y=240)
        c9=Checkbutton(FF1, text='Strawberry',variable=var9)
        c9.place(x=10,y=270)
        l9=Label(FF1,text='20 ')
        l9.place(x=220,y=270)
        sp9=Spinbox(FF1,from_=1,to=100,width='10')
        sp9.place(x=130,y=270)
        c10=Checkbutton(FF1, text='Ocean Water',variable=var10)
        c10.place(x=10,y=300)
        l10=Label(FF1,text='20 ')
        l10.place(x=220,y=300)
        sp10=Spinbox(FF1,from_=1,to=100,width='10')
        sp10.place(x=130,y=300)
        c11=Checkbutton(FF1, text='Passionfruit',variable=var11)
        c11.place(x=10,y=330)
        l11=Label(FF1,text='20 ')
        l11.place(x=220,y=330)
        sp11=Spinbox(FF1,from_=1,to=100,width='10')
        sp11.place(x=130,y=330)
        c12=Checkbutton(FF1, text='Oreos',variable=var12)
        c12.place(x=10,y=360)
        l12=Label(FF1,text='20 ')
        l12.place(x=220,y=360)
        sp12=Spinbox(FF1,from_=1,to=100,width='10')
        sp12.place(x=130,y=360)
        c13=Checkbutton(FF1, text='Sprinkles ',variable=var13)
        c13.place(x=10,y=390)
        l13=Label(FF1,text='20 ')
        l13.place(x=220,y=390)
        sp13=Spinbox(FF1,from_=1,to=100,width='10')
        sp13.place(x=130,y=390)
        c14=Checkbutton(FF1, text='Sea Salt',variable=var14)
        c14.place(x=10,y=420)
        l14=Label(FF1,text='20 ')
        l14.place(x=220,y=420)
        sp14=Spinbox(FF1,from_=1,to=100,width='10')
        sp14.place(x=130,y=420)
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

        #---------------Food----------------
        FF2 = Frame(root,bd=2,width=318,height=470,bg='#0B4C5F')
        FF2.place(x=321,y=30)
        t = Label(FF2,text='Food',font=('tomato',15,BOLD),bg='#0B4C5F',fg='gold')
        t.place(x=120,y=0)
        var15 = BooleanVar()
        var16 = BooleanVar()
        var17 = BooleanVar()
        var18 = BooleanVar()
        var19 = BooleanVar()
        var20 = BooleanVar()
        var21 = BooleanVar()
        var22 = BooleanVar()
        var23 = BooleanVar()
        var24 = BooleanVar()
        var25 = BooleanVar()
        var26 = BooleanVar()
        var27 = BooleanVar()
        var28 = BooleanVar()
        c11=Checkbutton(FF2, text='Toast',variable=var15)
        c11.place(x=10,y=30)
        l11=Label(FF2,text='20 ')
        l11.place(x=220,y=30)
        sp11=Spinbox(FF2,from_=1,to=100,width='10')
        sp11.place(x=130,y=30)
        c21=Checkbutton(FF2, text='Red Sauce Pizza',variable=var16)
        c21.place(x=10,y=60)
        l21=Label(FF2,text='20 ')
        l21.place(x=220,y=60)
        sp21=Spinbox(FF2,from_=1,to=100,width='10')
        sp21.place(x=130,y=60)
        c31=Checkbutton(FF2, text='Baps',variable=var17)
        c31.place(x=10,y=90)
        l31=Label(FF2,text='20 ')
        l31.place(x=220,y=90)
        sp31=Spinbox(FF2,from_=1,to=100,width='10')
        sp31.place(x=130,y=90)
        c41=Checkbutton(FF2, text='Croissants',variable=var18)
        c41.place(x=10,y=120)
        l41=Label(FF2,text='20 ')
        l41.place(x=220,y=120)
        sp41=Spinbox(FF2,from_=1,to=100,width='10')
        sp41.place(x=130,y=120)
        c51=Checkbutton(FF2, text='Assorted Wraps',variable=var19)
        c51.place(x=10,y=150)
        l51=Label(FF2,text='20 ')
        l51.place(x=220,y=150)
        sp51=Spinbox(FF2,from_=1,to=100,width='10')
        sp51.place(x=130,y=150)
        c61=Checkbutton(FF2, text='Assorted Paninis',variable=var20)
        c61.place(x=10,y=180)
        l61=Label(FF2,text='20 ')
        l61.place(x=220,y=180)
        sp61=Spinbox(FF2,from_=1,to=100,width='10')
        sp61.place(x=130,y=180)
        c71=Checkbutton(FF2, text='Chicken Toasties',variable=var21)
        c71.place(x=10,y=210)
        l71=Label(FF2,text='20 ')
        l71.place(x=220,y=210)
        sp71=Spinbox(FF2,from_=1,to=100,width='10')
        sp71.place(x=130,y=210)
        c81=Checkbutton(FF2, text='Assorted Quiches',variable=var22)
        c81.place(x=10,y=240)
        l81=Label(FF2,text='20 ')
        l81.place(x=220,y=240)
        sp81=Spinbox(FF2,from_=1,to=100,width='10')
        sp81.place(x=130,y=240)
        c91=Checkbutton(FF2, text='Assorted Salads',variable=var23)
        c91.place(x=10,y=270)
        l91=Label(FF2,text='20 ')
        l91.place(x=220,y=270)
        sp91=Spinbox(FF2,from_=1,to=100,width='10')
        sp91.place(x=130,y=270)
        c101=Checkbutton(FF2, text='Greek Pizza',variable=var24)
        c101.place(x=10,y=300)
        l101=Label(FF2,text='20 ')
        l101.place(x=220,y=300)
        sp101=Spinbox(FF2,from_=1,to=100,width='10')
        sp101.place(x=130,y=300)
        c111=Checkbutton(FF2, text='SUPER MELTS',variable=var25)
        c111.place(x=10,y=330)
        l111=Label(FF2,text='20 ')
        l111.place(x=220,y=330)
        sp111=Spinbox(FF2,from_=1,to=100,width='10')
        sp111.place(x=130,y=330)
        c121=Checkbutton(FF2, text='Grilled Shrimp',variable=var26)
        c121.place(x=10,y=360)
        l121=Label(FF2,text='20 ')
        l121.place(x=220,y=360)
        sp121=Spinbox(FF2,from_=1,to=100,width='10')
        sp121.place(x=130,y=360)
        c131=Checkbutton(FF2, text='Greek Salad',variable=var27)
        c131.place(x=10,y=390)
        l131=Label(FF2,text='20 ')
        l131.place(x=220,y=390)
        sp131=Spinbox(FF2,from_=1,to=100,width='10')
        sp131.place(x=130,y=390)
        c141=Checkbutton(FF2, text='Fish Sandwich',variable=var28)
        c141.place(x=10,y=420)
        l141=Label(FF2,text='20 ')
        l141.place(x=220,y=420)
        sp141=Spinbox(FF2,from_=1,to=100,width='10')
        sp141.place(x=130,y=420)
        c11.deselect()
        c21.deselect()
        c31.deselect()
        c41.deselect()
        c51.deselect()
        c61.deselect()
        c71.deselect()
        c81.deselect()
        c91.deselect()
        c101.deselect()
        c111.deselect()
        c121.deselect()
        c131.deselect()
        c141.deselect()
        

        #-----------------Cafe & Soda--------------------
        FF3 = Frame(root,bd=2,width=318,height=470,bg='#0B4C5F')
        FF3.place(x=641,y=30)
        t = Label(FF3,text='Cafe & Soda',font=('tomato',15,BOLD),bg='#0B4C5F',fg='gold')
        t.place(x=120,y=0)
        var11 = BooleanVar()
        var21 = BooleanVar()
        var31 = BooleanVar()
        var41 = BooleanVar()
        var51 = BooleanVar()
        var61 = BooleanVar()
        var71 = BooleanVar()
        var81 = BooleanVar()
        var91 = BooleanVar()
        var101 = BooleanVar()
        var111 = BooleanVar()
        var121 = BooleanVar()
        var131 = BooleanVar()
        var141 = BooleanVar()
        c12 = Checkbutton(FF3, text='Cappuccino', variable=var11)
        c12.deselect()
        c12.place(x=10, y=30)
        l12 = Label(FF3, text='20 ')
        l12.place(x=220, y=30)
        sp12 = Spinbox(FF3, from_=1, to=100, width='10')
        sp12.place(x=130, y=30)
        c22 = Checkbutton(FF3, text='Short Machinator', variable=var21)
        c22.deselect()
        c22.place(x=10, y=60)
        l22 = Label(FF3, text='20 ')
        l22.place(x=220, y=60)
        sp22 = Spinbox(FF3, from_=1, to=100, width='10')
        sp22.place(x=130, y=60)
        c32 = Checkbutton(FF3, text='Long Machinator', variable=var31)
        c32.deselect()
        c32.place(x=10, y=90)
        l32 = Label(FF3, text='20 ')
        l32.place(x=220, y=90)
        sp32 = Spinbox(FF3, from_=1, to=100, width='10')
        sp32.place(x=130, y=90)
        c42 = Checkbutton(FF3, text='Affogato', variable=var41)
        c42.deselect()
        c42.place(x=10, y=120)
        l42 = Label(FF3, text='20 ')
        l42.place(x=220, y=120)
        sp42 = Spinbox(FF3, from_=1, to=100, width='10')
        sp42.place(x=130, y=120)
        c52 = Checkbutton(FF3, text='Piccolo Latte', variable=var51)
        c52.deselect()
        c52.place(x=10, y=150)
        l52 = Label(FF3, text='20 ')
        l52.place(x=220, y=150)
        sp52 = Spinbox(FF3, from_=1, to=100, width='10')
        sp52.place(x=130, y=150)
        c62 = Checkbutton(FF3, text='Flavoured Latte', variable=var61)
        c62.deselect()
        c62.place(x=10, y=180)
        l62 = Label(FF3, text='20 ')
        l62.place(x=220, y=180)
        sp62 = Spinbox(FF3, from_=1, to=100, width='10')
        sp62.place(x=130, y=180)
        c72 = Checkbutton(FF3, text='Glace', variable=var71)
        c72.deselect()
        c72.place(x=10, y=210)
        l72 = Label(FF3, text='20 ')
        l72.place(x=220, y=210)
        sp72 = Spinbox(FF3, from_=1, to=100, width='10')
        sp72.place(x=130, y=210)
        c82 = Checkbutton(FF3, text='Latte', variable=var81)
        c82.deselect()
        c82.place(x=10, y=240)
        l82 = Label(FF3, text='20 ')
        l82.place(x=220, y=240)
        sp82 = Spinbox(FF3, from_=1, to=100, width='10')
        sp82.place(x=130, y=240)
        c92 = Checkbutton(FF3, text='Mocha', variable=var91)
        c92.deselect()
        c92.place(x=10, y=270)
        l92 = Label(FF3, text='20 ')
        l92.place(x=220, y=270)
        sp92 = Spinbox(FF3, from_=1, to=100, width='10')
        sp92.place(x=130, y=270)
        c102 = Checkbutton(FF3, text='Milk', variable=var101)
        c102.deselect()
        c102.place(x=10, y=300)
        l102 = Label(FF3, text='20 ')
        l102.place(x=220, y=300)
        sp102 = Spinbox(FF3, from_=1, to=100, width='10')
        sp102.place(x=130, y=300)
        c112 = Checkbutton(FF3, text='maple', variable=var111)
        c112.deselect()
        c112.place(x=10, y=330)
        l112 = Label(FF3, text='20 ')
        l112.place(x=220, y=330)
        sp112 = Spinbox(FF3, from_=1, to=100, width='10')
        sp112.place(x=130, y=330)
        c122 = Checkbutton(FF3, text='Spices', variable=var121)
        c122.deselect()
        c122.place(x=10, y=360)
        l122 = Label(FF3, text='20 ')
        l122.place(x=220, y=360)
        sp122 = Spinbox(FF3, from_=1, to=100, width='10')
        sp122.place(x=130, y=360)
        c132 = Checkbutton(FF3, text='Coca powder', variable=var131)
        c132.deselect()
        c132.place(x=10, y=390)
        l132 = Label(FF3, text='20 ')
        l132.place(x=220, y=390)
        sp132 = Spinbox(FF3, from_=1, to=100, width='10')
        sp132.place(x=130, y=390)
        c142 = Checkbutton(FF3, text='Vanilla', variable=var141)
        c142.deselect()
        c142.place(x=10, y=420)
        l142 = Label(FF3, text='20 ')
        l142.place(x=220, y=420)
        sp142 = Spinbox(FF3, from_=1, to=100, width='10')
        sp142.place(x=130, y=420)
        #----------function to get data from user------------
        def order():
            user_order = []
            if var1.get() == True:
                user_order.append(sp1.get() + ' ' + c1['text']+'    ' + str(int(l1['text']) * int(sp1.get())) + ' EGP')
            if var2.get() == True:
                user_order.append(sp2.get() + ' ' + c2['text']+'    ' + str(int(l2['text']) * int(sp2.get())) + ' EGP')
            if var3.get():
                user_order.append(sp3.get() + ' ' + c3['text']+'    ' + str(int(l3['text']) * int(sp3.get())) + ' EGP')
            if var4.get() == True:
                user_order.append(sp4.get() + ' ' + c4['text']+'    ' + str(int(l4['text']) * int(sp4.get())) + ' EGP')
            if var5.get() == True:
                user_order.append(sp5.get() + ' ' + c5['text']+'    ' + str(int(l5['text']) * int(sp5.get())) + ' EGP')
            if var6.get() == True:
                user_order.append(sp6.get() + ' ' + c6['text']+'    ' + str(int(l6['text']) * int(sp6.get())) + ' EGP')
            if var7.get() == True:
                user_order.append(sp7.get() + ' ' + c7['text']+'    ' + str(int(l7['text']) * int(sp7.get())) + ' EGP')
            if var8.get() == True:
                user_order.append(sp8.get() + ' ' + c8['text']+'    ' + str(int(l8['text']) * int(sp8.get())) + ' EGP')
            if var9.get() == True:
                user_order.append(sp9.get() + ' ' + c9['text']+'    ' + str(int(l9['text']) * int(sp9.get())) + ' EGP')
            if var10.get() == True:
                user_order.append(sp10.get() + ' ' + c10['text']+'    ' + str(int(l10['text']) * int(sp10.get())) + ' EGP')
            if var11.get() == True:
                user_order.append(sp11.get() + ' ' + c11['text']+'    ' + str(int(l11['text']) * int(sp11.get())) + ' EGP')
            if var12.get() == True:
                user_order.append(sp12.get() + ' ' + c12['text']+'    ' + str(int(l12['text']) * int(sp12.get())) + ' EGP')
            if var13.get() == True:
                user_order.append(sp13.get() + ' ' + c13['text']+'    ' + str(int(l13['text']) * int(sp13.get())) + ' EGP')
            if var14.get() == True:
                user_order.append(sp14.get() + ' ' + c14['text']+'    ' + str(int(l14['text']) * int(sp14.get())) + ' EGP')  



            if var15.get() == True:
                user_order.append(sp11.get() + ' ' + c11['text']+'    ' + str(int(l11['text']) * int(sp11.get())) + ' EGP')
            if var16.get() == True:
                user_order.append(sp21.get() + ' ' + c21['text']+'    ' + str(int(l21['text']) * int(sp21.get())) + ' EGP')
            if var17.get():
                user_order.append(sp31.get() + ' ' + c31['text']+'    ' + str(int(l31['text']) * int(sp31.get())) + ' EGP')
            if var18.get() == True:
                user_order.append(sp41.get() + ' ' + c41['text']+'    ' + str(int(l41['text']) * int(sp41.get())) + ' EGP')
            if var19.get() == True:
                user_order.append(sp51.get() + ' ' + c51['text']+'    ' + str(int(l51['text']) * int(sp51.get())) + ' EGP')
            if var20.get() == True:
                user_order.append(sp61.get() + ' ' + c61['text']+'    ' + str(int(l61['text']) * int(sp61.get())) + ' EGP')
            if var21.get() == True:
                user_order.append(sp71.get() + ' ' + c71['text']+'    ' + str(int(l71['text']) * int(sp71.get())) + ' EGP')
            if var22.get() == True:
                user_order.append(sp81.get() + ' ' + c81['text']+'    ' + str(int(l81['text']) * int(sp81.get())) + ' EGP')
            if var23.get() == True:
                user_order.append(sp91.get() + ' ' + c91['text']+'    ' + str(int(l91['text']) * int(sp91.get())) + ' EGP')
            if var24.get() == True:
                user_order.append(sp101.get() + ' ' + c101['text']+'    ' + str(int(l101['text']) * int(sp101.get())) + ' EGP')
            if var25.get() == True:
                user_order.append(sp11.get() + ' ' + c111['text']+'    ' + str(int(l111['text']) * int(sp111.get())) + ' EGP')
            if var26.get() == True:
                user_order.append(sp121.get() + ' ' + c121['text']+'    ' + str(int(l121['text']) * int(sp121.get())) + ' EGP')
            if var27.get() == True:
                user_order.append(sp131.get() + ' ' + c131['text']+'    ' + str(int(l131['text']) * int(sp131.get())) + ' EGP')
            if var28.get() == True:
                user_order.append(sp141.get() + ' ' + c141['text']+'    ' + str(int(l141['text']) * int(sp141.get())) + ' EGP')
                    
            if var11.get() == True:
                user_order.append(sp12.get() + ' ' + c12['text']+'    ' + str(int(l12['text']) * int(sp12.get())) + ' EGP')
            if var21.get() == True:
                user_order.append(sp22.get() + ' ' + c22['text']+'    ' + str(int(l22['text']) * int(sp22.get())) + ' EGP')
            if var31.get():
                user_order.append(sp32.get() + ' ' + c32['text']+'    ' + str(int(l32['text']) * int(sp32.get())) + ' EGP')
            if var41.get() == True:
                user_order.append(sp42.get() + ' ' + c42['text']+'    ' + str(int(l42['text']) * int(sp42.get())) + ' EGP')
            if var51.get() == True:
                user_order.append(sp52.get() + ' ' + c52['text']+'    ' + str(int(l52['text']) * int(sp52.get())) + ' EGP')
            if var61.get() == True:
                user_order.append(sp62.get() + ' ' + c62['text']+'    ' + str(int(l62['text']) * int(sp62.get())) + ' EGP')
            if var71.get() == True:
                user_order.append(sp72.get() + ' ' + c72['text']+'    ' + str(int(l72['text']) * int(sp72.get())) + ' EGP')
            if var81.get() == True:
                user_order.append(sp82.get() + ' ' + c82['text']+'    ' + str(int(l82['text']) * int(sp82.get())) + ' EGP')
            if var91.get() == True:
                user_order.append(sp92.get() + ' ' + c92['text']+'    ' + str(int(l92['text']) * int(sp92.get())) + ' EGP')
            if var101.get() == True:
                user_order.append(sp102.get() + ' ' + c102['text']+'    ' + str(int(l102['text']) * int(sp102.get())) + ' EGP')
            if var111.get() == True:
                user_order.append(sp112.get() + ' ' + c112['text']+'    ' + str(int(l112['text']) * int(sp112.get())) + ' EGP')
            if var121.get() == True:
                user_order.append(sp122.get() + ' ' + c122['text']+'    ' + str(int(l122['text']) * int(sp122.get())) + ' EGP')
            if var131.get() == True:
                user_order.append(sp132.get() + ' ' + c132['text']+'    ' + str(int(l132['text']) * int(sp132.get())) + ' EGP')
            if var141.get() == True:
                user_order.append(sp142.get() + ' ' + c142['text']+'    ' + str(int(l142['text']) * int(sp142.get())) + ' EGP')     
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

            if var15.get() == True:
                tp += int(l11['text']) * int(sp11.get())
            if var16.get() == True:
                tp += int(l21['text']) * int(sp21.get())
            if var17.get() == True:
                tp += int(l31['text']) * int(sp31.get())
            if var18.get() == True:
                tp += int(l41['text']) * int(sp41.get())
            if var19.get() == True:
                tp += int(l51['text']) * int(sp51.get())
            if var20.get() == True:
                tp += int(l61['text']) * int(sp61.get())
            if var21.get() == True:
                tp += int(l71['text']) * int(sp71.get())
            if var22.get() == True:
                tp += int(l81['text']) * int(sp81.get())
            if var23.get() == True:
                tp += int(l91['text']) * int(sp91.get())
            if var24.get() == True:
                tp += int(l101['text']) * int(sp101.get())
            if var25.get() == True:
                tp += int(l111['text']) * int(sp111.get())
            if var26.get() == True:
                tp += int(l121['text']) * int(sp121.get())
            if var27.get() == True:
                tp += int(l131['text']) * int(sp131.get())
            if var28.get() == True:
                tp += int(l141['text']) * int(sp141.get())


            if var11.get() == True:
                tp += int(l12['text']) * int(sp12.get())
            if var21.get() == True:
                tp += int(l22['text']) * int(sp22.get())
            if var31.get() == True:
                tp += int(l32['text']) * int(sp32.get())
            if var41.get() == True:
                tp += int(l42['text']) * int(sp42.get())
            if var51.get() == True:
                tp += int(l52['text']) * int(sp52.get())
            if var61.get() == True:
                tp += int(l62['text']) * int(sp62.get())
            if var71.get() == True:
                tp += int(l72['text']) * int(sp72.get())
            if var81.get() == True:
                tp += int(l82['text']) * int(sp82.get())
            if var91.get() == True:
                tp += int(l92['text']) * int(sp92.get())
            if var101.get() == True:
                tp += int(l102['text']) * int(sp102.get())
            if var111.get() == True:
                tp += int(l112['text']) * int(sp112.get())
            if var121.get() == True:
                tp += int(l122['text']) * int(sp122.get())
            if var131.get() == True:
                tp += int(l132['text']) * int(sp132.get())
            if var141.get() == True:
                tp += int(l142['text']) * int(sp142.get())
                # test code
                tkinter.messagebox.showinfo('Total price', tp)
        Submit = Button(F3,text='Submit',font=('tomato',10,BOLD),bg='#0B4C5F',fg='white',width=15,height=2,command=order)
        Submit.place(x=270,y=20)




root = Tk()
ob = Restaurant(root)   
root.mainloop()
