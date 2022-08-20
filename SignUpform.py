from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import backend_db

# helper function to center the window
def resize_and_center(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")

# style
window_width = 500
window_height = 300
font_normal = font=('Tahoma', 14)
font_bold = font=('Tahoma', 14, 'bold')
color_submit = 'blue'
padx = 10
pady = 10

# create window
root = Tk()
root.title('Restaurant Bot')
root.resizable(False, False)
resize_and_center(root, width=window_width, height=window_height)


# create container
container = Frame(root)


def signUpButton():
    flag=False
    username=ent_username.get()
    password=ent_password.get()
    conformed_password=ent_confirmed.get()
    
    result=backend_db.showAllUsers()
    for row in result:
        if row[0]==username:
            flag=True
            
    if flag==True:
        tkinter.messagebox.askokcancel('System','user name alread taken')
        return
        
    if flag==False:
        if password==conformed_password:
             backend_db.addUser(username, password)
             root.destroy()
             import History
        else:
            tkinter.messagebox.askokcancel('System','you must write the same password in two fields')
            ent_confirmed.delete(0,END)
            ent_password.delete(0,END)
                 
# create widgets inside container
lbl_username = Label(container, text='username', font=font_bold)
lbl_password = Label(container, text='password', font=font_bold)
lbl_confirmed = Label(container, text='Confirm password', font=font_bold)
ent_username = Entry(container, font=font_normal)
ent_password = Entry(container, show='*', font=font_normal)
ent_confirmed = Entry(container, show='*', font=font_normal)
btn_signup = Button(container, text='Sign Up', font=font_bold, fg=color_submit,command=signUpButton)

# place widgets in a grid (3 rows, 2 cols)
lbl_username.grid(column=0, row=0, padx=padx, pady=pady)
lbl_password.grid(column=0, row=1, padx=padx, pady=pady)
lbl_confirmed.grid(column=0, row=2, padx=padx, pady=pady)

ent_username.grid(column=1, row=0, padx=padx, pady=pady)
ent_password.grid(column=1, row=1, padx=padx, pady=pady)
ent_confirmed.grid(column=1, row=2, padx=padx, pady=pady)

btn_signup.grid(column=0, row=3, columnspan=2, sticky='EW', padx=padx, pady=pady)

# center the container inside the window
container.place(relx=0.5, rely=0.5, anchor='c')

root.mainloop()
