import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3
import os
import webbrowser
import backend


class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("SERVER LOGIN")
        self.master.geometry("350x250")
        self.master["bg"] = "#1C2833"
        self.message = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        lb = tk.Label(self.master, text="forgot password", bg="#1C2833", fg="white",font=('Arial', 12, "bold"))
        lb.place(x=235, y=172)
        lb.bind('<Button-1>', self.route) 
        tk.Label(self.master, width="300", text="Login From", bg="#0E6655", fg="white",
              font=("Arial", 12, "bold")).pack()
        tk.Label(self.master, text="Username * ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=20, y=40)
        tk.Entry(self.master, textvariable=self.username, bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=120, y=42, anchor='w')
        tk.Label(self.master, text="Password * ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=20, y=80)
        tk.Entry(self.master, textvariable=self.password, show="*", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=120, y=82, anchor='w')
        tk.Label(self.master, text="", textvariable=self.message, bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=95, y=120)
        tk.Button(self.master, text="Login", width=10, height=1, command=self.login,bg="#0E6655",
               font=("Arial", 12, "bold")).place(x=125, y=170)
        tk.Button(self.master, text="Register", width=10, height=1, command=self.register, bg="#0E6655",
               font=("Arial", 12, "bold")).place(x=125, y=210)
        


    def route(self,event=None):
        uname = self.username.get()
        
        if uname=='':
            self.message.set("Enter valid username")

        else:
            print(f"Mrs.{uname}, you have been redirected to web-server, please refresh your webbrowser")
            backend.redirect(uname)
            self.message.set("Please login again")


    def login(self):
        uname=self.username.get()
        pwd=self.password.get()

        if uname=='' or pwd=='':
            self.message.set("fill the empty field!!!")

        else:
            backend.login_db(uname, pwd)

            self.message.set("Exited from the Server")
                
            

    def register(self):
        uname=self.username.get()
        pwd=self.password.get()
        
        if uname=='' or pwd=='':
            self.message.set("fill the empty field!!!")

        else:
            backend.register_db(uname, pwd)

            self.message.set(f"Successfully Registered as {uname}")

        
    
root = tk.Tk()
LoginForm(root)
root.mainloop()
