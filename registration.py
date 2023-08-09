import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import messagebox 

registration_window = Tk()
registration_window.geometry("600x400")
registration_window.configure(background="#364F6B")

firebase = firebase.FirebaseApplication("https://d-login-system-4b651-default-rtdb.firebaseio.com/", None)

def login(): 
    print("login function")
    
def register(): 
    print("register function")
    reg_user = username_entry.get()
    reg_password = password_entry.get()
    print(reg_user)
    print(reg_password)
    b_password = reg_password.encode()
    e_password = hashlib.md5(b_password)
    print(e_password)
    hex_password = e_password.hexdigest()
    print(hex_password)
    firebase.put("/", reg_user, hex_password)
    messagebox.showinfo("Status", "Registered Successfully")
    
def login_window():
    login_window = Tk()
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register to LillBud Clothing Corner" , font = ("Century Gothic", "25", "bold"), bg="#FC5185")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg="#FC5185")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg="#FC5185")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window, show = "*")
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()