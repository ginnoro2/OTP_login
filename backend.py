
import sqlite3
import webbrowser
import os
import sys

#defining login function
def login_db(uname, pwd):
    conn = sqlite3.connect('student.db') 
    cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))

    result =  cursor.fetchone()
    conn.close()

    if result:
        print(f"logged in as {uname}")
        dock()

    else:

        print("Invalid credentials")


def dock():
    os.system('docker run --rm -it -p 5000:80 ubuntu:latest bin/bash')
       
       
def redirect(uname):
    conn = sqlite3.connect('student.db')
    cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s"'%(uname))

    if cursor.fetchone():
        for i in range(0, 4):

            webbrowser.open("http://localhost:5000")
            browser()

        
def browser():
    os.system('python3 app.py')
#defining loginform function

  

def register_db(uname, pwd):
    conn = sqlite3.connect('student.db') 
    conn.execute("""INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES (?, ?)""",(uname, pwd))

    conn.commit()
    print(f"your username is {uname}")
    print(f"your password is {pwd}")
    
    conn.close()

    
    

    



