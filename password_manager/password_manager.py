



import tkinter
from tkinter import *
import mysql.connector
#import encryption 

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

    login_file_readonly = open("..\\password_manager\\logins.txt","r")

    #verify login now
    if username_entry.get() in login_file_readonly.read():
        login_file_readonly = open("..\\password_manager\\logins.txt","r")
        if password_entry.get() in login_file_readonly.read():

            passwords_window= Toplevel(tk)
            passwords_window.title("Passwords")
            passwords_window.geometry("790x450")

    
            L3 = Label(passwords_window, text="New Website name")
            L3.grid(row=0 ,column=0)
            new_website_entry = Entry(passwords_window)
            new_website_entry.grid(row=0 ,column=1)

            L3 = Label(passwords_window, text="New Username")
            L3.grid(row=0 ,column=2)
            new_username_entry = Entry(passwords_window)
            new_username_entry.grid(row=0 ,column=3)

            L3 = Label(passwords_window, text="New Password")
            L3.grid(row=0 ,column=4)
            new_password_entry = Entry(passwords_window)
            new_password_entry.grid(row=0 ,column=5)

            def add_data():

                ext_website_entry = new_website_entry.get()
                ext_username_entry = new_username_entry.get()
                ext_password_entry = new_password_entry.get()

                database = mysql.connector.connect(host="localhost", user="admin", passwd="admin", database="passprofiles")
                db_cursor = database.cursor()
                querry = "insert into profiles values('{}','{}','{}')".format(ext_website_entry,ext_username_entry,ext_password_entry)
                db_cursor.execute(querry)
                db_cursor.execute("commit")
                print('success')

            def fetchdata():

                database = mysql.connector.connect(host="localhost", user="admin", passwd="admin",database="passprofiles")
                db_cursor = database.cursor()
                db_cursor.execute("select * from profile")
                lst0 = db_cursor.fetchall()
                db_cursor.close()
                database.close()
                output = ''
                for x in lst0:
                    output = output + x[0] + '  |' + x[1] + '  |' + x[2] + '\n'
                print(output)
                return output

            text = Text(passwords_window, height=10, width=80)
            text.grid(row=7, columnspan=5)

            add_password_button = Button(passwords_window, text="fetchdata",command=lambda: text.insert(END, fetchdata()))
            add_password_button.grid(row=4, column=3)

            add_password_button = Button(passwords_window, text="Add Data",command=add_data)
            add_password_button.grid(row=3, column=3)

        else:
            print("incorrect password")
    else:
        print("invalid credentials")
    #gotta work here above

login_button = Button(tk, text ="LOGIN",command=login)
login_button.grid(row=3, column=1)


def open_register_page():

    regwindow=Toplevel(tk)
    regwindow.title("REGISTER")
    regwindow.geometry("250x200")

    Label(regwindow,text="Username").grid(row=2, column=0)
    new_registration_username_entry = Entry(regwindow, bd=5)
    new_registration_username_entry.grid(row=2, column=1)

    Label(regwindow, text="Password").grid(row=3, column=0)
    new_registration_password_entry = Entry(regwindow, bd=5)
    new_registration_password_entry.grid(row=3, column=1)

    def register():
        extracting_username = new_registration_username_entry.get()
        extracting_password = new_registration_password_entry.get()

        global login_file
        login_file = open("..\\password_manager\\logins.txt","a+")
        login_file_readonly = open("..\\password_manager\\logins.txt","r")

        if extracting_username in login_file_readonly.read():
            print("This username is already chosen, please choose another username.")

        else:
            login_file = open("..\\password_manager\\logins.txt","a+")
            login_file.write(extracting_username + "\n")
            login_file.write(extracting_password + "\n")
            login_file.close()
            tk.quit()

    register_button = Button(regwindow, text="REGISTER",command=register)
    register_button.grid(row=6, column=1)

register_button = Button(tk, text ="REGISTER",command=open_register_page)
register_button.grid(row=4, column=1)


tk.mainloop()