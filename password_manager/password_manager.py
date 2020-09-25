

import tkinter
from tkinter import *

tk = tkinter.Tk()
tk.title("Password Manager")
tk.geometry('300x300')

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

login_button = Button(tk, text ="LOGIN")
login_button.grid(row=3, column=1)


def openregister():

    regwindow=Toplevel(tk)
    regwindow.title("REGISTER")
    regwindow.geometry("250x200")

    Label(regwindow,text="Username").grid(row=2, column=0)
    new_username_entry = Entry(regwindow, bd=5)
    new_username_entry.grid(row=2, column=1)

    Label(regwindow, text="Password").grid(row=3, column=0)
    new_password_entry = Entry(regwindow, bd=5)
    new_password_entry.grid(row=3, column=1)


    extracting_username = new_username_entry.get()
    extracting_password = new_password_entry.get()
    print(extracting_username)
    print(extracting_password)

    def register():

        passwords_file = open("..\\password_manager\\passwords.txt","w")
        passwords_file.write(extracting_username)
        passwords_file.write(extracting_password)
        passwords_file.close()
        tk.quit()

    register_button = Button(regwindow, text="REGISTER",command=register)
    register_button.grid(row=6, column=1)


register_button = Button(tk, text ="REGISTER",command=openregister)
register_button.grid(row=4, column=1)
tk.mainloop()