from flask import Flask, render_template, request,flash
app = Flask(__name__)

import datetime
import mysql.connector
conn = mysql.connector.connect(database="cricket", user="project", host="127.0.0.1",
        password="Cricket.1")
cursor = conn.cursor(buffered=True)
cursor1 = conn.cursor(buffered=True)
#Even if previous user didn't logout, current_user will be cleared.
f=open("current_user.txt","w")
f.write("0")
f.close()

@app.route('/')
@app.route('/login.html')
def login_page(name=None):
    return render_template('login.html', name=name)

#just add a logout button and add link /logout.html
@app.route('/logout.html')
def logout(name=None):
    f=open("current_user.txt","w")
    f.write("0")
    f.close() #redirect to login page 
    return render_template('login.html', name=name)

@app.route('/price.html')
def pllist(name=None):
    cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player")
    rows = [i for i in cursor]
    return render_template('price.html', name=name, rows=rows)

@app.route('/price.html', methods=['POST','GET'])
def plist(name=None):
    print("here")
    if request.form['send_button'] == 'Batting Style':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by batstyle DESC")
    elif request.form['send_button'] == 'Matches':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by matches DESC")
    elif request.form['send_button'] == 'Runs':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by runs DESC")
    elif request.form['send_button'] == 'Highest Score':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by highest_score DESC")
    elif request.form['send_button'] == 'Average':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by average DESC")
    elif request.form['send_button'] == 'Strike Rate':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by strike_rate DESC")
    elif request.form['send_button'] == 'Hundreds':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by hundreds DESC")
    elif request.form['send_button'] == 'Fifties':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by fifties DESC")
    elif request.form['send_button'] == 'Fours':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by fours DESC")
    elif request.form['send_button'] == 'Sixes':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by sixes DESC")
    else:
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player")
    rows = [i for i in cursor]
    return render_template('price.html', name=name, rows=rows)

@app.route('/administrator.html')
def ulist(name=None):
    cursor.execute("select * from users;")
    rows = [i for i in cursor]
    return render_template('administrator.html', name=name, rows=rows)

@app.route('/schedule.html')
def sched(name=None):    
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    cursor1.execute("""select team1_id, team2_id, dates, ground_id from matches where dates > '%s';""" % (date))
    ans = []
    new = cursor1.fetchone()
    while new:
        a = []
        team1 = new[0]
        team2 = new[1]
        ground = new[3]
        cursor.execute("""select name from team where team_id = '%d';""" %(team1))
        t = cursor.fetchone()
        a.append(t[0])

        cursor.execute("""select name from team where team_id = '%d';""" %(team2))
        t = cursor.fetchone()
        a.append(t[0])

        a.append(new[2])

        cursor.execute("""select name from ground where ground_id = '%d';""" %(ground))
        t = cursor.fetchone()
        a.append(t[0])
        ans.append(a)
        new = cursor1.fetchone()

    return render_template('schedule.html', name=name, ans=ans)


@app.route('/home.html')
def matchinfo(name=None):
    return render_template('home.html', name=name)

@app.route('/', methods=['POST','GET'])
@app.route('/login.html', methods=['POST','GET'])
def login_page_post(name=None):
    username, password = request.form['username'],request.form['password']
    cursor.execute(("select password, user_id from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        return render_template('login.html', name=name,error1="Incorrect username",error2="")
    if a[0] == password:
        f=open("current_user.txt","w")
        f.write(str(a[1]))
        f.close()
        print("user_id is"+str(a[1]))
        return render_template('home.html', name=name)
    else:
        return  render_template('login.html', name=name,error2="Incorrect Password",error1="")

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
        return  render_template('registration.html', name=name,error="Passwords do not match")
    cursor.execute(("select password from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        cursor.execute(("insert into users(username, password,firstname,lastname, email, favteam) values('{}','{}','{}','{}','{}','{}');".format(username, password,firstname,lastname, email, favteam)))
        cursor.execute(("commit;"))
        cursor.execute(("select user_id from users where username ='{}';".format(username)))
        a = cursor.fetchone()
        f=open("current_user.txt","w")
        f.write(str(a[0]))
        f.close()
        print("user_id is"+str(a[0]))
        return render_template('home.html', name=name)
    else:
        return  render_template('registration.html', name=name,error="Username is already taken!")

@app.route('/creategroup.html')
def create_group_page(name=None):
    f=open("current_user.txt","r")
    user_id=f.read()
    f.close()
    if not user_id:
        return render_template('login.html', name=name)
    return render_template('creategroup.html', name=name)

@app.route('/creategroup.html', methods=['POST','GET'])
def create_group(name=None):
    grpname = request.form['grpname']
    cursor.execute(("select group_id from groups where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    if a:
        return render_template('creategroup.html', name=name,error="Group name is already taken!")
    cursor.execute(("insert into groups(groupname) values('{}');".format(grpname)))
    cursor.execute(("commit;"))
    cursor.execute(("select group_id from groups where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    group_id = a[0]
    f=open("current_user.txt","r")
    user_id=f.read()
    f.close()
    cursor.execute(("insert into user_group(user_id, group_id) values('{}','{}');".format(user_id, group_id)))
    cursor.execute(("commit;"))
    return render_template('addtogroup.html', name=name)

@app.route('/addtogroup.html')
def addto_group_page(name=None):
    f=open("current_user.txt","r")
    user_id=f.read()
    f.close()
    if not user_id:
        return render_template('login.html', name=name)
    return render_template('addtogroup.html', name=name)

@app.route('/addtogroup.html', methods=['POST','GET'])
def addto_group(name=None):
    username = request.form['username']
    grpname="sdf"#get it from html page
    cursor.execute(("select user_id from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        return render_template('addtogroup.html', name=name,error="Invalid username")
    else:
        uid = a[0]
    cursor.execute(("select group_id from group where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    gid = a[0]
    cursor.execute(("select * from user_group where (user_id='{}' and group_id='{}');".format(uid,gid)))
    a = cursor.fetchone()
    if not a:
        return render_template('addtogroup.html', name=name,error="User is already part of group!")
    cursor.execute(("insert into user_group values('{}','{}');".format(uid,gid)))
    cursor.execute(("commit;"))
    return render_template('addtogroup.html', name=name)
