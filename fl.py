from flask import Flask, render_template, request
app = Flask(__name__)

import mysql.connector
conn = mysql.connector.connect(database="cricket", user="project", host="127.0.0.1",
        password="Cricket.1")
cursor = conn.cursor()

@app.route('/')
@app.route('/login.html')
def login_page(name=None):
    return render_template('login.html', name=name)

@app.route('/afterlogin.html')
def aflogin(name=None):
    return render_template('afterlogin.html', name=name)

@app.route('/price.html')
def plist(name=None):
    cursor.execute("select * from users")
    rows = [i for i in cursor]
    return render_template('price.html', name=name, rows=rows)

@app.route('/home.html')
def matchinfo(name=None):
    return render_template('home.html', name=name)

@app.route('/', methods=['POST','GET'])
@app.route('/login.html', methods=['POST','GET'])
def login_page_post(name=None):
    username, password = request.form['username'],request.form['password']
    cursor.execute(("select password from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        return ("Incorrect username")
    if a[0] == password:
        return ("Hello {}, you've successfully logged in".format(username))
    else:
        return ("Incorrect Password")

@app.route('/registration.html')
def registration_page(name=None):
    return render_template('registration.html', name=name)


@app.route('/registration.html', methods=['POST','GET'])
def registration_page_post(name=None):
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    email = request.form['emailid']
    favteam = request.form['favouriteteam']
    password = request.form['password']
    cpassword = request.form['cpassword']
    if password != cpassword:
        return ("Password does not match")
    cursor.execute(("select password from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        cursor.execute(("insert into users(username, password,firstname,lastname, email, favteam) values('{}','{}','{}','{}','{}','{}');".format(username, password,firstname,lastname, email, favteam)))
        cursor.execute(("commit;"))
        return ("Hello {}, you've successfully registered".format(username))
    else:
        return ("Username is already taken!")
