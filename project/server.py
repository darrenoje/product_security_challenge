from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import html, re, bcrypt
from flask_wtf.csrf import CSRFProtect
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
salt = bcrypt.gensalt()
csrf = CSRFProtect()
csrf.init_app(app)
db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True) 
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    attempts = db.Column(db.Integer)

    def __init__(self, name, password, attempts):
        self.name = name
        self.password = password
        self.attempts = attempts


def sanitiseInput(input):
    sanitised = html.escape(input)
    return sanitised

def allowedPassword(input):
    m = re.compile(r'[a-zA-Z0-9]*$')
    if m.match(input) and validPasswordLength(input):
        return True
    else:
        return False

def validPasswordLength(input):
    if len(input) < 6:
        return False
    else:
        return True

def commonPassword(input):
    if input in d.keys():
        return True
    else:
        return False
    

@app.route("/create-acc", methods=["POST", "GET"])
def create_acc():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["pw"]
        legal_password = allowedPassword(password)
        
        if legal_password:
            if not commonPassword(password):
                hashed_password = bcrypt.hashpw(password.encode(), salt)
                new_user = users(user, hashed_password, 0)
                db.session.add(new_user)
                db.session.commit()
                flash("Your account is successfully created!", "info")
                return redirect(url_for("home")) 
            else:
                flash("Please use a stronger password!", "info")
                return render_template("create-acc.html")
        else:
            flash("Please ensure that your username contains only alphabets, password has at least 6 characters that may consist of alphabets and numbers", "info")
            return render_template("create-acc.html")
    else:
        return render_template("create-acc.html")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        password = sanitiseInput(request.form["pw"])
        registered_user = users.query.filter_by(name=user).first()
        if registered_user:
            if registered_user.attempts >= 5:
                flash("Your account has been locked out due to multiple failures of login.")
                return render_template("index.html")
            if bcrypt.checkpw(password.encode(), registered_user.password):    
                response = redirect(url_for("user"))
                response.set_cookie
                return redirect(url_for("user"))    
            else:
                registered_user.attempts += 1
                db.session.commit()
                flash("Username or password is wrong! Kindly check again", "info")
                return redirect(url_for("home"))
        else:
            flash("Username or password is wrong! Kindly check again", "info")
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/user")
def user():
    return f"<h1>Welcome!</h1>"


if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    d = dict()
    common_passwords = open('10k-most-common-passwords.txt', 'r')
    for line in open('10k-most-common-passwords.txt', 'r').readlines():
        d[line.strip()] = 1
    
    app.run(ssl_context=('adhoc'), debug=False)
    