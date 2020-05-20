from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()


def save():
    acc_name=account_name.get()
    acc=account.get()
    note=passw.get()
    file1=open(username,"a+")
    file1.write("\n"+acc_name+": ")  
    file1.write('Username= '+acc)
    file1.write(' Password= '+note+"\n")
    file1.close()
    Label(screen9,text="Saved!",fg="green",font=("Calibri",11)).pack()

def view_acc():
    file1=open(username,"r")
    screen11=Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("300x250")
    Label(screen11,text="All Accounts:\n").pack()
    
    data=file1.read()
    Label(screen11,text=data).pack()
    file1.close()
    
    

def create_account():
    global screen9
    global account_name
    account_name=StringVar()
    global account
    account=StringVar()
    global passw
    passw=StringVar()

    screen9=Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x250")
    Label(screen9,text="Enter Account Name").pack()
    Entry(screen9,textvariable=account_name).pack()
    Label(screen9,text="Enter username to add").pack()
    Entry(screen9,textvariable=account).pack()
    Label(screen9,text="Enter Password to add").pack()
    Entry(screen9,textvariable=passw).pack()
    Button(screen9,text="Save",command=save).pack()

def session():
    screen8=Toplevel(screen)
    screen8.title("Info")
    screen8.geometry("400x400")
    Label(screen8,text="Welcome To The Dashboard").pack()
    Button(screen8,text="Add Account",command=create_account).pack()
    Button(screen8,text="View All Acounts",command=view_acc).pack()
    Button(screen8,text="Delete Account",command=delete2).pack()
    

def login_success():
    session()
    
def password_fail():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Login")
    screen4.geometry("150x100")
    Label(screen4,text="Password Error").pack()
    Button(screen4,text="OK",command=delete3).pack()

def no_user():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("Login")
    screen5.geometry("150x100")
    Label(screen5,text="User not found").pack()
    Button(screen5,text="OK",command=delete4).pack()

def register_user(): 
    username_info=username.get()
    password_info=password.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info+"\n\n")
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registration Successful",fg="green",font=("Calibri",11)).pack()    

def login_verify():
    global username
    username=username_verify.get()
    password=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    listfiles=os.listdir()
    if username in listfiles:
        file1=open(username,"r+")
        verify=file1.read().splitlines()
        if password in verify:
            file1.close()
            login_success()
        else:
            password_fail()
    else:
        no_user()

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()

    Label(screen1,text="Please Enter Details Below").pack()
    Label(screen1,text="").pack()

    Label(screen1,text="Username *").pack()

    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password *").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()

    Button(screen1,text="Register",width="10",height="1",command=register_user).pack()
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2,text="Please Enter Login Details Below").pack()
    Label(screen2,text="").pack()

    global username_verify
    global password_verify
    
    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2,text="Username *").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password *").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width=10,height=1,command=login_verify).pack()
    

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.1")
    Label(text="notes 1.0",bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",height="2",width="30",command=register).pack()

    screen.mainloop()

main_screen()

