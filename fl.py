from flask import Flask, render_template, request
app = Flask(__name__)

import psycopg2
conn = psycopg2.connect(database="cricket", user="project", host="127.0.0.1",
        password="cricket", port="5432")
cursor = conn.cursor()

@app.route('/')
@app.route('/login.html')
def login_page(name=None):
    return render_template('login.html', name=name)


@app.route('/', methods=['POST','GET'])
@app.route('/login.html', methods=['POST','GET'])
def login_page_post(name=None):
    username, password = request.form['username'],request.form['password']
    try:
        cursor.execute(("select password from users where name ='{}';".format(username)))
    except:
        cursor.execute(("rollback;"))
    cursor.execute(("select password from users where name ='{}';".format(username)))
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
    fav = request.form['favouriteteam']
    password = request.form['password']
    cpassword = request.form['cpassword']
    if password != cpassword:
        return ("Password does not match")
    try:
        cursor.execute(("select password from users where name ='{}';".format(username)))
    except:
        cursor.execute(("rollback;"))
    cursor.execute(("select password from users where name ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        try:
            cursor.execute(("insert into users(name, password) values('{}', '{}');".format(username, password)))
        except:
            cursor.execute(("rollback;"))
        cursor.execute(("insert into users(name,password) values('{}', '{}');".format(username, password)))
        return ("Hello {}, you've successfully registered".format(username))
    else:
        return ("Username is already taken!")





"""
insert into users(name,password) values('aditya','asdfg');
@app.route('/p')
def hell_word(name=None):
    a = ["asd;lfk","afgth","tyjytd"]
    return render_template("c.html",name=name,rows=a)
"""
