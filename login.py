from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import backEnd_DB


# helper function to center the window
def resize_and_center(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")


# style
window_width = 500
window_height = 300
font_normal = font = ('Tahoma', 14)
font_bold = font = ('Tahoma', 14, 'bold')
color_submit = 'blue'
padx = 10
pady = 10

# create window
root = Tk()
root.title('Restaurant Bot')
root.resizable(False, False)
resize_and_center(root, width=window_width, height=window_height)

# *************************************************   create data base **************
backEnd_DB.logintable()
# ******************************************************************************************

# create container
container = Frame(root)
# backEnd_DB.addUser("admin","karim123")

def loginButton():
    flag = False
    username = ent_username.get()
    password = ent_password.get()

    result = backEnd_DB.showAllUsers()
    for row in result:
        if row[0] == username and row[1] == password:
            flag = True
            root.destroy()
            import History
    if flag == False:
        tkinter.messagebox.askokcancel('System', 'Incorrect username or password')
        ent_username.delete(0, END)
        ent_password.delete(0, END)


# create widgets inside container
lbl_username = Label(container, text='username', font=font_bold)
lbl_password = Label(container, text='password', font=font_bold)
ent_username = Entry(container, font=font_normal)
ent_password = Entry(container, show='*', font=font_normal)
btn_login = Button(container, text='Login', font=font_bold, fg=color_submit, command=loginButton)


# place widgets in a grid (3 rows, 2 cols)
lbl_username.grid(column=0, row=0, padx=padx, pady=pady)
lbl_password.grid(column=0, row=1, padx=padx, pady=pady)
ent_username.grid(column=1, row=0, padx=padx, pady=pady)
ent_password.grid(column=1, row=1, padx=padx, pady=pady)
btn_login.grid(column=0, row=2, columnspan=2, sticky='EW', padx=padx, pady=pady)


# center the container inside the window
container.place(relx=0.5, rely=0.5, anchor='c')

root.mainloop()
