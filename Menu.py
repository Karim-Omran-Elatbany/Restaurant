import tkinter.messagebox
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Treeview

import backEnd_DB


# center the main window according to screen
class Restaurant:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x600+30+10")
        self.root.title('Restaurant Bot')
        self.root.resizable(False, False)
        # self.root.iconbitmap('E:\\Restaurant-main\\Images\\restaurant.ico')
        title = Label(root, text='Restaurant Menu', fg='white', bg='#0B2F3A', font=('tomato', 15))
        title.pack(fill=X)

        # ------------BUttons------------------------------------------
        F3 = Frame(self.root, bd=2, width=753, height=100, bg='#0B4C5F')
        F3.place(x=1, y=500)

        Exit = Button(F3, text='Exit', font=('tomato', 10, BOLD), bg='#0B4C5F', fg='white', width=15, height=2,
                      command=root.destroy)
        Exit.place(x=450, y=20)

        # ------------------------IceCream--------------------------------
        FF1 = Frame(root, bd=2, width=250, height=470, bg='#0B4C5F')
        FF1.place(x=1, y=30)
        t = Label(FF1, text='IceCream', font=('tomato', 15, BOLD), bg='#0B4C5F', fg='gold')
        t.place(x=90, y=0)
        var1_for_icecream = BooleanVar()
        var2_for_icecream = BooleanVar()
        var3_for_icecream = BooleanVar()
        var4_for_icecream = BooleanVar()
        var5_for_icecream = BooleanVar()
        var6_for_icecream = BooleanVar()
        var7_for_icecream = BooleanVar()
        var8_for_icecream = BooleanVar()
        var9_for_icecream = BooleanVar()
        var10_for_icecream = BooleanVar()
        var11_for_icecream = BooleanVar()
        var12_for_icecream = BooleanVar()
        var13_for_icecream = BooleanVar()
        var14_for_icecream = BooleanVar()
        ice_cream1 = Checkbutton(FF1, text='Gummy Bears', variable=var1_for_icecream)
        ice_cream1.place(x=10, y=30)
        price_for_icecream1 = Label(FF1, text='10 ')
        price_for_icecream1.place(x=220, y=30)
        number_of_icecream1 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream1.place(x=130, y=30)

        ice_cream2 = Checkbutton(FF1, text='Mint Chip', variable=var2_for_icecream)
        ice_cream2.place(x=10, y=60)
        price_for_icecream2 = Label(FF1, text='20 ')
        price_for_icecream2.place(x=220, y=60)
        number_of_icecream2 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream2.place(x=130, y=60)

        ice_cream3 = Checkbutton(FF1, text='Salted Caramel', variable=var3_for_icecream)
        ice_cream3.place(x=10, y=90)
        price_for_icecream3 = Label(FF1, text='15 ')
        price_for_icecream3.place(x=220, y=90)
        number_of_icecream3 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream3.place(x=130, y=90)

        ice_cream4 = Checkbutton(FF1, text='Chocolate ', variable=var4_for_icecream)
        ice_cream4.place(x=10, y=120)
        price_for_icecream4 = Label(FF1, text='30 ')
        price_for_icecream4.place(x=220, y=120)
        number_of_icecream4 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream4.place(x=130, y=120)

        ice_cream5 = Checkbutton(FF1, text='Vanilla Bean', variable=var5_for_icecream)
        ice_cream5.place(x=10, y=150)
        price_for_icecream5 = Label(FF1, text='20 ')
        price_for_icecream5.place(x=220, y=150)
        number_of_icecream5 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream5.place(x=130, y=150)

        ice_cream6 = Checkbutton(FF1, text='Coffee Oreo ', variable=var6_for_icecream)
        ice_cream6.place(x=10, y=180)
        price_for_icecream6 = Label(FF1, text='40 ')
        price_for_icecream6.place(x=220, y=180)
        number_of_icecream6 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream6.place(x=130, y=180)

        ice_cream7 = Checkbutton(FF1, text='Reeses Pieces', variable=var7_for_icecream)
        ice_cream7.place(x=10, y=210)
        price_for_icecream7 = Label(FF1, text='50 ')
        price_for_icecream7.place(x=220, y=210)
        number_of_icecream7 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream7.place(x=130, y=210)

        ice_cream8 = Checkbutton(FF1, text='Peanut Butter', variable=var8_for_icecream)
        ice_cream8.place(x=10, y=240)
        price_for_icecream8 = Label(FF1, text='22 ')
        price_for_icecream8.place(x=220, y=240)
        number_of_icecream8 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream8.place(x=130, y=240)

        ice_cream9 = Checkbutton(FF1, text='Strawberry', variable=var9_for_icecream)
        ice_cream9.place(x=10, y=270)
        price_for_icecream9 = Label(FF1, text='35 ')
        price_for_icecream9.place(x=220, y=270)
        number_of_icecream9 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream9.place(x=130, y=270)

        ice_cream10 = Checkbutton(FF1, text='Ocean Water', variable=var10_for_icecream)
        ice_cream10.place(x=10, y=300)
        price_for_icecream10 = Label(FF1, text='29 ')
        price_for_icecream10.place(x=220, y=300)
        number_of_icecream10 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream10.place(x=130, y=300)

        ice_cream11 = Checkbutton(FF1, text='Passionfruit', variable=var11_for_icecream)
        ice_cream11.place(x=10, y=330)
        price_for_icecream11 = Label(FF1, text='35 ')
        price_for_icecream11.place(x=220, y=330)
        number_of_icecream11 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream11.place(x=130, y=330)

        ice_cream12 = Checkbutton(FF1, text='Oreos', variable=var12_for_icecream)
        ice_cream12.place(x=10, y=360)
        price_for_icecream12 = Label(FF1, text='55 ')
        price_for_icecream12.place(x=220, y=360)
        number_of_icecream12 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream12.place(x=130, y=360)

        ice_cream13 = Checkbutton(FF1, text='Sprinkles ', variable=var13_for_icecream)
        ice_cream13.place(x=10, y=390)
        price_for_icecream13 = Label(FF1, text='20 ')
        price_for_icecream13.place(x=220, y=390)
        number_of_icecream13 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream13.place(x=130, y=390)

        ice_cream14 = Checkbutton(FF1, text='Sea Salt', variable=var14_for_icecream)
        ice_cream14.place(x=10, y=420)
        price_for_icecream14 = Label(FF1, text='10 ')
        price_for_icecream14.place(x=220, y=420)
        number_of_icecream14 = Spinbox(FF1, from_=1, to=100, width=10)
        number_of_icecream14.place(x=130, y=420)

        ice_cream1.deselect()
        ice_cream2.deselect()
        ice_cream3.deselect()
        ice_cream4.deselect()
        ice_cream5.deselect()
        ice_cream6.deselect()
        ice_cream7.deselect()
        ice_cream8.deselect()
        ice_cream9.deselect()
        ice_cream10.deselect()
        ice_cream11.deselect()
        ice_cream12.deselect()
        ice_cream13.deselect()
        ice_cream14.deselect()

        # ---------------Food----------------
        FF2 = Frame(root, bd=2, width=250, height=470, bg='#0B4C5F')
        FF2.place(x=252, y=30)
        t = Label(FF2, text='Food', font=('tomato', 15, BOLD), bg='#0B4C5F', fg='gold')
        t.place(x=90, y=0)
        var1_for_food = BooleanVar()
        var2_for_food = BooleanVar()
        var3_for_food = BooleanVar()
        var4_for_food = BooleanVar()
        var5_for_food = BooleanVar()
        var6_for_food = BooleanVar()
        var7_for_food = BooleanVar()
        var8_for_food = BooleanVar()
        var9_for_food = BooleanVar()
        var10_for_food = BooleanVar()
        var11_for_food = BooleanVar()
        var12_for_food = BooleanVar()
        var13_for_food = BooleanVar()
        var14_for_food = BooleanVar()

        food1 = Checkbutton(FF2, text='Toast', variable=var1_for_food)
        food1.place(x=10, y=30)
        price_for_food1 = Label(FF2, text='120 ')
        price_for_food1.place(x=220, y=30)
        number_of_food1 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food1.place(x=130, y=30)

        food2 = Checkbutton(FF2, text='Red Sauce Pizza', variable=var2_for_food)
        food2.place(x=10, y=60)
        price_for_food2 = Label(FF2, text='130 ')
        price_for_food2.place(x=220, y=60)
        number_of_food2 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food2.place(x=130, y=60)

        food3 = Checkbutton(FF2, text='Baps', variable=var3_for_food)
        food3.place(x=10, y=90)
        price_for_food3 = Label(FF2, text='140 ')
        price_for_food3.place(x=220, y=90)
        number_of_food3 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food3.place(x=130, y=90)

        food4 = Checkbutton(FF2, text='Croissants', variable=var4_for_food)
        food4.place(x=10, y=120)
        price_for_food4 = Label(FF2, text='320 ')
        price_for_food4.place(x=220, y=120)
        number_of_food4 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food4.place(x=130, y=120)

        food5 = Checkbutton(FF2, text='Assorted Wraps', variable=var5_for_food)
        food5.place(x=10, y=150)
        price_for_food5 = Label(FF2, text='150 ')
        price_for_food5.place(x=220, y=150)
        number_of_food5 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food5.place(x=130, y=150)

        food6 = Checkbutton(FF2, text='Assorted Paninis', variable=var6_for_food)
        food6.place(x=10, y=180)
        price_for_food6 = Label(FF2, text='110 ')
        price_for_food6.place(x=220, y=180)
        number_of_food6 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food6.place(x=130, y=180)

        food7 = Checkbutton(FF2, text='Chicken Toasties', variable=var7_for_food)
        food7.place(x=10, y=210)
        price_for_food7 = Label(FF2, text='220 ')
        price_for_food7.place(x=220, y=210)
        number_of_food7 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food7.place(x=130, y=210)

        food8 = Checkbutton(FF2, text='Assorted Quiches', variable=var8_for_food)
        food8.place(x=10, y=240)
        price_for_food8 = Label(FF2, text='220 ')
        price_for_food8.place(x=220, y=240)
        number_of_food8 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food8.place(x=130, y=240)

        food9 = Checkbutton(FF2, text='Assorted Salads', variable=var9_for_food)
        food9.place(x=10, y=270)
        price_for_food9 = Label(FF2, text='330 ')
        price_for_food9.place(x=220, y=270)
        number_of_food9 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food9.place(x=130, y=270)

        food10 = Checkbutton(FF2, text='Greek Pizza', variable=var10_for_food)
        food10.place(x=10, y=300)
        price_for_food10 = Label(FF2, text='230 ')
        price_for_food10.place(x=220, y=300)
        number_of_food10 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food10.place(x=130, y=300)

        food11 = Checkbutton(FF2, text='SUPER MELTS', variable=var11_for_food)
        food11.place(x=10, y=330)
        price_for_food11 = Label(FF2, text='250 ')
        price_for_food11.place(x=220, y=330)
        number_of_food11 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food11.place(x=130, y=330)

        food12 = Checkbutton(FF2, text='Grilled Shrimp', variable=var12_for_food)
        food12.place(x=10, y=360)
        price_for_food12 = Label(FF2, text='150 ')
        price_for_food12.place(x=220, y=360)
        number_of_food12 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food12.place(x=130, y=360)

        food13 = Checkbutton(FF2, text='Greek Salad', variable=var13_for_food)
        food13.place(x=10, y=390)
        price_for_food13 = Label(FF2, text='160 ')
        price_for_food13.place(x=220, y=390)
        number_of_food13 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food13.place(x=130, y=390)

        food14 = Checkbutton(FF2, text='Fish Sandwich', variable=var14_for_food)
        food14.place(x=10, y=420)
        price_for_food14 = Label(FF2, text='180 ')
        price_for_food14.place(x=220, y=420)
        number_of_food14 = Spinbox(FF2, from_=1, to=100, width=10)
        number_of_food14.place(x=130, y=420)

        food1.deselect()
        food2.deselect()
        food3.deselect()
        food4.deselect()
        food5.deselect()
        food6.deselect()
        food7.deselect()
        food8.deselect()
        food9.deselect()
        food10.deselect()
        food11.deselect()
        food12.deselect()
        food13.deselect()
        food14.deselect()

        # -----------------Coffee & Soda--------------------
        FF3 = Frame(root, bd=2, width=250, height=470, bg='#0B4C5F')
        FF3.place(x=504, y=30)
        t = Label(FF3, text='Cafe & Soda', font=('tomato', 15, BOLD), bg='#0B4C5F', fg='gold')
        t.place(x=90, y=0)

        var1_for_drinks = BooleanVar()
        var2_for_drinks = BooleanVar()
        var3_for_drinks = BooleanVar()
        var4_for_drinks = BooleanVar()
        var5_for_drinks = BooleanVar()
        var6_for_drinks = BooleanVar()
        var7_for_drinks = BooleanVar()
        var8_for_drinks = BooleanVar()
        var9_for_drinks = BooleanVar()
        var10_for_drinks = BooleanVar()
        var11_for_drinks = BooleanVar()
        var12_for_drinks = BooleanVar()
        var13_for_drinks = BooleanVar()
        var14_for_drinks = BooleanVar()

        drink1 = Checkbutton(FF3, text='Cappuccino', variable=var1_for_drinks)
        drink1.place(x=10, y=30)
        price_for_drink1 = Label(FF3, text='10 ')
        price_for_drink1.place(x=220, y=30)
        number_of_drink1 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink1.place(x=130, y=30)

        drink2 = Checkbutton(FF3, text='Short Machinator', variable=var2_for_drinks)
        drink2.place(x=10, y=60)
        price_for_drink2 = Label(FF3, text='5 ')
        price_for_drink2.place(x=220, y=60)
        number_of_drink2 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink2.place(x=130, y=60)

        drink3 = Checkbutton(FF3, text='Long Machinator', variable=var3_for_drinks)
        drink3.place(x=10, y=90)
        price_for_drink3 = Label(FF3, text='10 ')
        price_for_drink3.place(x=220, y=90)
        number_of_drink3 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink3.place(x=130, y=90)

        drink4 = Checkbutton(FF3, text='Affogato', variable=var4_for_drinks)
        drink4.place(x=10, y=120)
        price_for_drink4 = Label(FF3, text='20 ')
        price_for_drink4.place(x=220, y=120)
        number_of_drink4 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink4.place(x=130, y=120)

        drink5 = Checkbutton(FF3, text='Piccolo Latte', variable=var5_for_drinks)
        drink5.place(x=10, y=150)
        price_for_drink5 = Label(FF3, text='25 ')
        price_for_drink5.place(x=220, y=150)
        number_of_drink5 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink5.place(x=130, y=150)

        drink6 = Checkbutton(FF3, text='Flavoured Latte', variable=var6_for_drinks)
        drink6.place(x=10, y=180)
        price_for_drink6 = Label(FF3, text='25 ')
        price_for_drink6.place(x=220, y=180)
        number_of_drink6 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink6.place(x=130, y=180)

        drink7 = Checkbutton(FF3, text='Glace', variable=var7_for_drinks)
        drink7.place(x=10, y=210)
        price_for_drink7 = Label(FF3, text='30 ')
        price_for_drink7.place(x=220, y=210)
        number_of_drink7 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink7.place(x=130, y=210)

        drink8 = Checkbutton(FF3, text='Latte', variable=var8_for_drinks)
        drink8.place(x=10, y=240)
        price_for_drink8 = Label(FF3, text='20 ')
        price_for_drink8.place(x=220, y=240)
        number_of_drink8 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink8.place(x=130, y=240)

        drink9 = Checkbutton(FF3, text='Mocha', variable=var9_for_drinks)
        drink9.place(x=10, y=270)
        price_for_drink9 = Label(FF3, text='35 ')
        price_for_drink9.place(x=220, y=270)
        number_of_drink9 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink9.place(x=130, y=270)

        drink10 = Checkbutton(FF3, text='Milk', variable=var10_for_drinks)
        drink10.place(x=10, y=300)
        price_for_drink10 = Label(FF3, text='40 ')
        price_for_drink10.place(x=220, y=300)
        number_of_drink10 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink10.place(x=130, y=300)

        drink11 = Checkbutton(FF3, text='maple', variable=var11_for_drinks)
        drink11.place(x=10, y=330)
        price_for_drink11 = Label(FF3, text='20 ')
        price_for_drink11.place(x=220, y=330)
        number_of_drink11 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink11.place(x=130, y=330)

        drink12 = Checkbutton(FF3, text='Spices', variable=var12_for_drinks)
        drink12.place(x=10, y=360)
        price_for_drink12 = Label(FF3, text='45 ')
        price_for_drink12.place(x=220, y=360)
        number_of_drink12 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink12.place(x=130, y=360)

        drink13 = Checkbutton(FF3, text='Coca powder', variable=var13_for_drinks)
        drink13.place(x=10, y=390)
        price_for_drink13 = Label(FF3, text='20 ')
        price_for_drink13.place(x=220, y=390)
        number_of_drink13 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink13.place(x=130, y=390)

        drink14 = Checkbutton(FF3, text='Vanilla', variable=var14_for_drinks)
        drink14.place(x=10, y=420)
        price_for_drink14 = Label(FF3, text='50 ')
        price_for_drink14.place(x=220, y=420)
        number_of_drink14 = Spinbox(FF3, from_=1, to=100, width=10)
        number_of_drink14.place(x=130, y=420)

        drink1.deselect()
        drink2.deselect()
        drink3.deselect()
        drink4.deselect()
        drink5.deselect()
        drink6.deselect()
        drink7.deselect()
        drink8.deselect()
        drink9.deselect()
        drink10.deselect()
        drink11.deselect()
        drink12.deselect()
        drink13.deselect()
        drink14.deselect()

        # ----------function to get data from user------------

        def total_price():
            tp = 0
            if var1_for_icecream.get():
                tp += int(price_for_icecream1['text']) * int(number_of_icecream1.get())
            if var2_for_icecream.get():
                tp += int(price_for_icecream2['text']) * int(number_of_icecream2.get())
            if var3_for_icecream.get():
                tp += int(price_for_icecream3['text']) * int(number_of_icecream3.get())
            if var4_for_icecream.get():
                tp += int(price_for_icecream4['text']) * int(number_of_icecream4.get())
            if var5_for_icecream.get():
                tp += int(price_for_icecream5['text']) * int(number_of_icecream5.get())
            if var6_for_icecream.get():
                tp += int(price_for_icecream6['text']) * int(number_of_icecream6.get())
            if var7_for_icecream.get():
                tp += int(price_for_icecream7['text']) * int(number_of_icecream7.get())
            if var8_for_icecream.get():
                tp += int(price_for_icecream8['text']) * int(number_of_icecream8.get())
            if var9_for_icecream.get():
                tp += int(price_for_icecream9['text']) * int(number_of_icecream9.get())
            if var10_for_icecream.get():
                tp += int(price_for_icecream10['text']) * int(number_of_icecream10.get())
            if var1_for_icecream.get():
                tp += int(price_for_icecream11['text']) * int(number_of_icecream11.get())
            if var12_for_icecream.get():
                tp += int(price_for_icecream12['text']) * int(number_of_icecream12.get())
            if var13_for_icecream.get():
                tp += int(price_for_icecream13['text']) * int(number_of_icecream13.get())
            if var14_for_icecream.get():
                tp += int(price_for_icecream14['text']) * int(number_of_icecream14.get())

            if var1_for_food.get():
                tp += int(price_for_food1['text']) * int(number_of_food1.get())
            if var2_for_food.get():
                tp += int(price_for_food2['text']) * int(number_of_food2.get())
            if var3_for_food.get():
                tp += int(price_for_food3['text']) * int(number_of_food3.get())
            if var4_for_food.get():
                tp += int(price_for_food4['text']) * int(number_of_food4.get())
            if var5_for_food.get():
                tp += int(price_for_food5['text']) * int(number_of_food5.get())
            if var6_for_food.get():
                tp += int(price_for_food6['text']) * int(number_of_food6.get())
            if var7_for_food.get():
                tp += int(price_for_food7['text']) * int(number_of_food7.get())
            if var8_for_food.get():
                tp += int(price_for_food8['text']) * int(number_of_food8.get())
            if var9_for_food.get():
                tp += int(price_for_food9['text']) * int(number_of_food9.get())
            if var10_for_food.get():
                tp += int(price_for_food10['text']) * int(number_of_food10.get())
            if var11_for_food.get():
                tp += int(price_for_food11['text']) * int(number_of_food11.get())
            if var12_for_food.get():
                tp += int(price_for_food12['text']) * int(number_of_food12.get())
            if var13_for_food.get():
                tp += int(price_for_food13['text']) * int(number_of_food13.get())
            if var14_for_food.get():
                tp += int(price_for_food14['text']) * int(number_of_food14.get())

            if var1_for_drinks.get():
                tp += int(price_for_drink1['text']) * int(number_of_drink1.get())
            if var2_for_drinks.get():
                tp += int(price_for_drink2['text']) * int(number_of_drink2.get())
            if var3_for_drinks.get():
                tp += int(price_for_drink3['text']) * int(number_of_drink3.get())
            if var4_for_drinks.get():
                tp += int(price_for_drink4['text']) * int(number_of_drink4.get())
            if var5_for_drinks.get():
                tp += int(price_for_drink5['text']) * int(number_of_drink5.get())
            if var6_for_drinks.get():
                tp += int(price_for_drink6['text']) * int(number_of_drink6.get())
            if var7_for_drinks.get():
                tp += int(price_for_drink7['text']) * int(number_of_drink7.get())
            if var8_for_drinks.get():
                tp += int(price_for_drink8['text']) * int(number_of_drink8.get())
            if var9_for_drinks.get():
                tp += int(price_for_drink9['text']) * int(number_of_drink9.get())
            if var10_for_drinks.get():
                tp += int(price_for_drink10['text']) * int(number_of_drink10.get())
            if var11_for_drinks.get():
                tp += int(price_for_drink11['text']) * int(number_of_drink11.get())
            if var12_for_drinks.get():
                tp += int(price_for_drink12['text']) * int(number_of_drink12.get())
            if var13_for_drinks.get():
                tp += int(price_for_drink13['text']) * int(number_of_drink13.get())
            if var14_for_drinks.get():
                tp += int(price_for_drink14['text']) * int(number_of_drink14.get())
                # test code
            return tp

        # ----------function to get data from user------------
        def order():
            user_order = []
            if var1_for_icecream.get():
                user_order.append(
                    number_of_icecream1.get() + ' ' + ice_cream1['text'] + '    ' + str(
                        int(price_for_icecream1['text']) * int(number_of_icecream1.get())) + ' EGP')

            if var2_for_icecream.get():
                user_order.append(
                    number_of_icecream2.get() + ' ' + ice_cream2['text'] + '    ' + str(
                        int(price_for_icecream2['text']) * int(number_of_icecream2.get())) + ' EGP')

            if var3_for_icecream.get():
                user_order.append(
                    number_of_icecream3.get() + ' ' + ice_cream3['text'] + '    ' + str(
                        int(price_for_icecream3['text']) * int(number_of_icecream3.get())) + ' EGP')

            if var4_for_icecream.get():
                user_order.append(
                    number_of_icecream4.get() + ' ' + ice_cream4['text'] + '    ' + str(
                        int(price_for_icecream4['text']) * int(number_of_icecream4.get())) + ' EGP')

            if var5_for_icecream.get():
                user_order.append(
                    number_of_icecream5.get() + ' ' + ice_cream5['text'] + '    ' + str(
                        int(price_for_icecream5['text']) * int(number_of_icecream5.get())) + ' EGP')

            if var6_for_icecream.get():
                user_order.append(
                    number_of_icecream6.get() + ' ' + ice_cream6['text'] + '    ' + str(
                        int(price_for_icecream6['text']) * int(number_of_icecream6.get())) + ' EGP')

            if var7_for_icecream.get():
                user_order.append(
                    number_of_icecream7.get() + ' ' + ice_cream7['text'] + '    ' + str(
                        int(price_for_icecream7['text']) * int(number_of_icecream7.get())) + ' EGP')
            if var8_for_icecream.get():
                user_order.append(
                    number_of_icecream8.get() + ' ' + ice_cream8['text'] + '    ' + str(
                        int(price_for_icecream8['text']) * int(number_of_icecream8.get())) + ' EGP')

            if var9_for_icecream.get():
                user_order.append(
                    number_of_icecream9.get() + ' ' + ice_cream9['text'] + '    ' + str(
                        int(price_for_icecream9['text']) * int(number_of_icecream9.get())) + ' EGP')

            if var10_for_icecream.get():
                user_order.append(
                    number_of_icecream10.get() + ' ' + ice_cream10['text'] + '    ' + str(
                        int(price_for_icecream10['text']) * int(number_of_icecream10.get())) + ' EGP')

            if var11_for_icecream.get():
                user_order.append(
                    number_of_icecream11.get() + ' ' + ice_cream11['text'] + '    ' + str(
                        int(price_for_icecream11['text']) * int(number_of_icecream11.get())) + ' EGP')

            if var12_for_icecream.get():
                user_order.append(
                    number_of_icecream12.get() + ' ' + ice_cream12['text'] + '    ' + str(
                        int(price_for_icecream12['text']) * int(number_of_icecream12.get())) + ' EGP')

            if var13_for_icecream.get():
                user_order.append(
                    number_of_icecream13.get() + ' ' + ice_cream13['text'] + '    ' + str(
                        int(price_for_icecream13['text']) * int(number_of_icecream13.get())) + ' EGP')

            if var14_for_icecream.get():
                user_order.append(
                    number_of_icecream14.get() + ' ' + ice_cream14['text'] + '    ' + str(
                        int(price_for_icecream14['text']) * int(number_of_icecream14.get())) + ' EGP')

            # ---------------Food----------------

            if var1_for_food.get():
                user_order.append(
                    number_of_food1.get() + ' ' + food1['text'] + '    ' + str(
                        int(price_for_food1['text']) * int(number_of_food1.get())) + ' EGP')

            if var2_for_food.get():
                user_order.append(
                    number_of_food2.get() + ' ' + food2['text'] + '    ' + str(
                        int(price_for_food2['text']) * int(number_of_food2.get())) + ' EGP')

            if var3_for_food.get():
                user_order.append(
                    number_of_food3.get() + ' ' + food3['text'] + '    ' + str(
                        int(price_for_food3['text']) * int(number_of_food3.get())) + ' EGP')

            if var4_for_food.get():
                user_order.append(
                    number_of_food4.get() + ' ' + food4['text'] + '    ' + str(
                        int(price_for_food4['text']) * int(number_of_food4.get())) + ' EGP')

            if var5_for_food.get():
                user_order.append(
                    number_of_food5.get() + ' ' + food5['text'] + '    ' + str(
                        int(price_for_food5['text']) * int(number_of_food5.get())) + ' EGP')

            if var6_for_food.get():
                user_order.append(
                    number_of_food6.get() + ' ' + food6['text'] + '    ' + str(
                        int(price_for_food6['text']) * int(number_of_food6.get())) + ' EGP')

            if var7_for_food.get():
                user_order.append(
                    number_of_food7.get() + ' ' + food7['text'] + '    ' + str(
                        int(price_for_food7['text']) * int(number_of_food7.get())) + ' EGP')

            if var8_for_food.get():
                user_order.append(
                    number_of_food8.get() + ' ' + food8['text'] + '    ' + str(
                        int(price_for_food8['text']) * int(number_of_food8.get())) + ' EGP')

            if var9_for_food.get():
                user_order.append(
                    number_of_food9.get() + ' ' + food9['text'] + '    ' + str(
                        int(price_for_food9['text']) * int(number_of_food9.get())) + ' EGP')

            if var10_for_food.get():
                user_order.append(
                    number_of_food10.get() + ' ' + food10['text'] + '    ' + str(
                        int(price_for_food10['text']) * int(number_of_food10.get())) + ' EGP')

            if var11_for_food.get():
                user_order.append(
                    number_of_food11.get() + ' ' + food11['text'] + '    ' + str(
                        int(price_for_food11['text']) * int(number_of_food11.get())) + ' EGP')

            if var12_for_food.get():
                user_order.append(
                    number_of_food12.get() + ' ' + food12['text'] + '    ' + str(
                        int(price_for_food12['text']) * int(number_of_food12.get())) + ' EGP')

            if var13_for_food.get():
                user_order.append(
                    number_of_food13.get() + ' ' + food13['text'] + '    ' + str(
                        int(price_for_food13['text']) * int(number_of_food13.get())) + ' EGP')

            if var14_for_food.get():
                user_order.append(
                    number_of_food14.get() + ' ' + food14['text'] + '    ' + str(
                        int(price_for_food14['text']) * int(number_of_food14.get())) + ' EGP')

                # ------------Drinks-------------------

            if var1_for_drinks.get():
                user_order.append(
                    number_of_drink1.get() + ' ' + drink1['text'] + '    ' + str(
                        int(price_for_drink1['text']) * int(number_of_drink1.get())) + ' EGP')

            if var2_for_drinks.get():
                user_order.append(
                    number_of_drink2.get() + ' ' + drink2['text'] + '    ' + str(
                        int(price_for_drink2['text']) * int(number_of_drink2.get())) + ' EGP')

            if var3_for_drinks.get():
                user_order.append(
                    number_of_drink3.get() + ' ' + drink3['text'] + '    ' + str(
                        int(price_for_drink3['text']) * int(number_of_drink3.get())) + ' EGP')

            if var4_for_drinks.get():
                user_order.append(
                    number_of_drink4.get() + ' ' + drink4['text'] + '    ' + str(
                        int(price_for_drink4['text']) * int(number_of_drink4.get())) + ' EGP')

            if var5_for_drinks.get():
                user_order.append(
                    number_of_drink5.get() + ' ' + drink5['text'] + '    ' + str(
                        int(price_for_drink5['text']) * int(number_of_drink5.get())) + ' EGP')

            if var6_for_drinks.get():
                user_order.append(
                    number_of_drink6.get() + ' ' + drink6['text'] + '    ' + str(
                        int(price_for_drink6['text']) * int(number_of_drink6.get())) + ' EGP')

            if var7_for_drinks.get():
                user_order.append(
                    number_of_drink7.get() + ' ' + drink7['text'] + '    ' + str(
                        int(price_for_drink7['text']) * int(number_of_drink7.get())) + ' EGP')

            if var8_for_drinks.get():
                user_order.append(
                    number_of_drink8.get() + ' ' + drink8['text'] + '    ' + str(
                        int(price_for_drink8['text']) * int(number_of_drink8.get())) + ' EGP')

            if var9_for_drinks.get():
                user_order.append(
                    number_of_drink9.get() + ' ' + drink9['text'] + '    ' + str(
                        int(price_for_drink9['text']) * int(number_of_drink9.get())) + ' EGP')

            if var10_for_drinks.get():
                user_order.append(
                    number_of_drink10.get() + ' ' + drink10['text'] + '    ' + str(
                        int(price_for_drink10['text']) * int(number_of_drink10.get())) + ' EGP')

            if var11_for_drinks.get():
                user_order.append(
                    number_of_drink11.get() + ' ' + drink11['text'] + '    ' + str(
                        int(price_for_drink11['text']) * int(number_of_drink11.get())) + ' EGP')

            if var12_for_drinks.get():
                user_order.append(
                    number_of_drink12.get() + ' ' + drink12['text'] + '    ' + str(
                        int(price_for_drink12['text']) * int(number_of_drink12.get())) + ' EGP')

            if var13_for_drinks.get():
                user_order.append(
                    number_of_drink13.get() + ' ' + drink13['text'] + '    ' + str(
                        int(price_for_drink13['text']) * int(number_of_drink13.get())) + ' EGP')

            if var14_for_drinks.get():
                user_order.append(
                    number_of_drink14.get() + ' ' + drink14['text'] + '    ' + str(
                        int(price_for_drink14['text']) * int(number_of_drink14.get())) + ' EGP')
            final_order = '\n'.join(user_order)
            if Ent_name.get() != '' or Ent_id.get() != '':
                backEnd_DB.addCustomer(Ent_name.get(), final_order, total_price())
                # ------------------------------------------------------------------------
                fetch_id = backEnd_DB.showAllCustomerID()
                user_id = fetch_id.fetchall()

                tree.insert('', END, values=(user_id[-1], Ent_name.get(), user_order[0], total_price()))
                for i in range(1, len(user_order)):
                    tree.insert('', END, values=('', '', user_order[i], ''))

            else:
                tkinter.messagebox.showerror('System', 'Please Enter Username')

        def search():
            rows = backEnd_DB.selectcustomer(Ent_id.get())
            for row in rows:
                tree.insert("", END, values=row)

        submit = Button(F3, text='Submit', font=('tomato', 10, BOLD), bg='#0B4C5F', fg='white', width=15, height=2,
                        command=order)
        submit.place(x=150, y=20)

        F1 = Frame(self.root, bd=2, width=547, height=100, bg='#0B4C5F')
        F1.place(x=755, y=500)
        t = Label(F1, text='Search For Customer', font=('tomato', 15, BOLD), bg='#0B4C5F', fg='gold')
        t.place(x=200, y=0)
        # ----------------------Search-----------------
        his_name = Label(F1, text='Username', font=('tomato', 10, BOLD), bg='#0B4C5F', fg='white')
        his_name.place(x=10, y=30)

        Ent_name = Entry(F1)
        Ent_name.place(x=90, y=33)

        his_id = Label(F1, text='ID', font=('tomato', 10, BOLD), bg='#0B4C5F', fg='white')
        his_id.place(x=10, y=60)

        Ent_id = Entry(F1)
        Ent_id.place(x=90, y=63)

        search = Button(F1, text='Search', font=('tomato', 10, BOLD), bg='#0B4C5F', fg='white', width=10,
                        height=2, command=search)
        search.place(x=430, y=30)

        # ---------F1--------------
        F1 = Label(F1, text='Restaurant Bot', font=('tomato', 13, BOLD), bg='#0B4C5F', fg='gold')
        F1.place(x=110, y=135)
        # ------------Output from User----------
        F2 = Frame(root, bd=2, width=400, height=400, bg='white')
        F2.place(x=760, y=30)
        columns = ['id', 'name', 'order', 'total price']
        tree = Treeview(F2, columns=columns, show='headings', height=22)
        scroll = Scrollbar(F2, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scroll.set)
        scroll.grid(row=0, column=1, sticky='ns')
        tree.column('id', width=50, anchor='center')
        tree.column('name', width=88, anchor='center')
        tree.column('order', width=300, anchor='center')
        tree.column('total price', width=80, anchor='center')
        tree.heading('id', text='id')
        tree.heading('name', text='name')
        tree.heading('order', text='order')
        tree.heading('total price', text='total price')
        tree.grid(column=0, row=0)

        backEnd_DB.showAllCustomerID()
        backEnd_DB.CustomerData()


root = Tk()
ob = Restaurant(root)
root.mainloop()
