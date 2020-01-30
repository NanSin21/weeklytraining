from flask import *
import sqlite3
from flask_paginate import Pagination, get_page_args
import os
from admin import admin
from task import tasktodo
from authenticate import auth
app = Flask(__name__, template_folder='template')
app.register_blueprint(admin)
app.register_blueprint(tasktodo)
app.register_blueprint(auth)
""" con = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="tododb"
) """


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    if 'aname' in session:
        username = session['aname']
        return render_template('about.html', username=username)

    if 'uname' in session:
        username = session['uname']
        return render_template('about.html', username=username)

    else:
        return redirect(url_for('home'))


@app.route("/remove", methods=["POST"])
def remove():
    msg = "msg"
    if request.method == "POST":
        uid = request.form["uid"]
        try:
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("delete from Interns where uid = ?", uid)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template(url_for('details'), msg)
            con.close()
    else:
        return "cannot remove user"


@app.route('/edit', methods=["POST"])
def edit():
    if request.method == "POST":
        uid = request.form["uid"]
        try:
            uname = request.form['uname']
            email = request.form['email']
            address = request.form['address']
            password = request.form['psw']
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("update Interns set uname=?, email=?, address=?, psw=?  where uid = ?",
                        (uname, email, address, password, uid))
            msg = "Intern record successfully updated"
        except:
            msg = "Intern can't be updated"
        finally:
            return render_template(url_for('details'), msg)
            con.close()
    else:
        return msg


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
