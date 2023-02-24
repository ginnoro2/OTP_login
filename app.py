from flask import *
from twilio.rest import Client
import random
import subprocess
import sqlite3

app = Flask(__name__)
app.secret_key = 'otp'#secret key session is written over cookies

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/validate_username', methods=['POST'])
def validate_username():
    uname = request.form['username']
    pwd = request.form['password']
    print(uname)
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    conn.execute("UPDATE ADMIN SET PASSWORD=? WHERE USERNAME=?", (pwd, uname))  
    conn.commit() 
    #return redirect(url_for('get_db'))
    return render_template('out.html')
    conn.close()
   
@app.route('/get_db', methods=['GET'])
def get_db():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor =  conn.execute('SELECT * FROM ADMIN')
    results = cursor.fetchall()
    print("ID\tUSERNAME\tPASSWORD")
    for row in cursor:
        print("{}\t{}\t{}".format(row[0], row[1], row[2]))

    conn.close()
    return results

#@app.route('/')
def result():
    get = get_db()
    print(get)
    
    return render_template('out.html',usr=get)

@app.route('/getOTP', methods = ['POST'])
def getOTP():
    number = request.form['number']
    val = getOTPApi(number)
    #if val:    
    #return render_template('login.html')
    return render_template('user.html')

@app.route('/validateOTP', methods = ['POST'])
def validateOTP():
    otp = request.form['otp']
    if 'response' in session:
        s= session['response']
        session.pop('response',None)
        if s == otp:
            #return redirect(url_for('get_db'))
            return render_template('user.html') 
            
        else:
            return render_template('server.html')

def generateOTP():
    return random.randrange(100000, 999999)

def getOTPApi(number):
    account_sid = 'ACc4ac69fcb07e679ef0d306f17c2fe316'
    auth_token = 'f7ee08df4a8a603dfa354abcc2901849'
    client = Client(account_sid, auth_token)
    otp = generateOTP()
    session['response'] = str(otp)
    body = 'Your OTP is    : ' + str(otp)
    message = client.messages.create(
                              body=body,
                              from_='+13855264732',
                              to=number
                          )
    if message.sid:
        True
    else:
        False

    print(message.sid)
def term():
    os.system('docker build -t testbuntu:latest .')

if __name__ == '__main__':
    app.run(debug=True)
