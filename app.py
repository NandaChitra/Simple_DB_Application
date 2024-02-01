from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/checkLogin", methods = ['POST'])
def checkLogin():
    uid = request.form["userid"]
    pwd = request.form["password"]
    if uid == 'admin' and pwd == 'admin':
        return render_template('LoginSuccess.html')
    else:
        return render_template('LoginError.html')

@app.route("/Display")
def Display():
    try:
        db_connect = mysql.connect(
            host="localhost", database="studentdatabase", user="root", passwd="admin", use_pure=True)
        sql = "Select USN, Name from Student1"
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        rs = mycursor.fetchall()
        return render_template('Show.html', rs=rs)
    except Exception as err:
        msg = 'Error in Database Access'
        return render_template('index.html', msg=msg)

app.run()
    
