

import tkinter
from tkinter import *
import mysql.connector

database= mysql.connector.connect(host="localhost",user="admin",passwd="admin",database="passprofiles")
db_cursor= database.cursor()
db_cursor.execute("show tables")
for table in db_cursor:
    print(table)

tk = tkinter.Tk()
tk.title("Password Manager")
tk.geometry('300x300')


icon_pic = PhotoImage(file = '..\images\keypic.png')
tk.iconphoto(False, icon_pic)
locker_pic = Canvas(tk,width = 125,height = 125)
locker_pic.grid(row=0, column=1)
image1 = PhotoImage(file='..\images\lockerpic.png')
locker_pic.create_image(20,20, anchor=NW, image=image1)

L1 = Label(tk, text="User Name").grid(row=1, column=0)
username_entry = Entry(tk, bd =5)
username_entry.grid(row=1, column=1)
L2 = Label(tk, text="Password").grid(row=2, column=0)
password_entry = Entry(tk, bd =5)
password_entry.grid(row=2, column=1)

def login():

    passwords_window= Toplevel(tk)
    passwords_window.title("Passwords")
    passwords_window.geometry("700x450")

    scrollbar_vertical = Scrollbar(passwords_window)
    scrollbar_vertical.grid(row=0 ,column=1)
    scrollbar_horizontal = Scrollbar(passwords_window, orient='horizontal')
    scrollbar_horizontal.grid(row=1 ,column=0)

    add_password_button = Button(passwords_window, text="Add Password")
    add_password_button.grid(row= 2, column= 0)

login_button = Button(tk, text ="LOGIN",command=login)
login_button.grid(row=3, column=1)


def open_register_page():

    regwindow=Toplevel(tk)
    regwindow.title("REGISTER")
    regwindow.geometry("250x200")

    Label(regwindow,text="Username").grid(row=2, column=0)
    new_username_entry = Entry(regwindow, bd=5)
    new_username_entry.grid(row=2, column=1)

    Label(regwindow, text="Password").grid(row=3, column=0)
    new_password_entry = Entry(regwindow, bd=5)
    new_password_entry.grid(row=3, column=1)

    def register():

        extracting_username = new_username_entry.get()
        extracting_password = new_password_entry.get()

        passwords_file = open("..\\password_manager\\passwords.txt","w")
        passwords_file.write(extracting_username)
        passwords_file.write(" ")
        passwords_file.write(extracting_password)
        passwords_file.close()
        tk.quit()

    register_button = Button(regwindow, text="REGISTER",command=register)
    register_button.grid(row=6, column=1)


register_button = Button(tk, text ="REGISTER",command=open_register_page)
register_button.grid(row=4, column=1)


tk.mainloop()