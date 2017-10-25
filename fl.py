from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/login.html')
def login_page(name=None):
    return render_template('login.html', name=name)


@app.route('/', methods=['POST','GET'])
@app.route('/login.html', methods=['POST','GET'])
def login_page_post(name=None):
    username, password = request.form['username'],request.form['password']
    return ("Hello {}, you've successfully logged in".format(username))







"""
@app.route('/p')
def hell_word(name=None):
    a = ["asd;lfk","afgth","tyjytd"]
    return render_template("c.html",name=name,rows=a)
"""
