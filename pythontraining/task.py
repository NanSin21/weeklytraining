from flask import *
import sqlite3
from flask_paginate import Pagination, get_page_args
import os

tasktodo = Blueprint('tasktodo', __name__, template_folder='template')

############ Task Insertion by User Page ###########
@tasktodo.route('/task', methods=['POST', 'GET'])
def task():
    msg = "msg"
    if request.method == "POST":
        if 'uname' in session:
            username = session['uname']
        try:
            todo = request.form['todo']
            datime = request.form['datet']
            details = request.form['descrip']

            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT COUNT(1) FROM Interns WHERE uname = ?;", [
                        username])  # CHECKS IF USERNAME EXSIST
            if cur.fetchone()[0]:
                cur.execute("SELECT uid FROM Interns WHERE uname = ?;", [
                            username])  # FETCH THE uid
            for row in cur.fetchall():
                uid = row[0]
                print(uid)
            cur.execute("INSERT into Tasks (todo, datime, details, uid) values (?,?,?,?)",
                        (todo, datime, details, uid))
            con.commit()

            msg = "Task successfully Added"
        except:
            con.rollback()
            msg = "We can not add the tasks to the list"
        finally:
            return render_template("/tasks/task.html", msg=msg)
            con.close()
    else:
        return render_template('/tasks/task.html')

############ Task view by User Page ###########
@tasktodo.route("/view")
def view():
    con = sqlite3.connect("todo.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Tasks")
    rows = cur.fetchall()

    return render_template("/tasks/todo.html", rows=rows)
    con.close()

############ Task Deletion by User Page ###########
@tasktodo.route("/delete", methods=["POST"])
def delete():
    msg = "msg"
    if request.method == "POST":
        tid = request.form["tid"]
        try:
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("delete from Tasks where tid = ?", tid)

            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return redirect(url_for('view'))
            con.close()
    else:
        return "No deletion process occured"

############ Task Updation by User Page ###########
@tasktodo.route('/update', methods=["POST"])
def update():

    if request.method == "POST":
        tid = request.form["tid"]
        try:
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            todo = request.form['todo']
            datime = request.form['datet']
            details = request.form['descrip']
            cur.execute("update Tasks set todo=?, datime=?, details=?  where tid = ?",
                        (todo, datime, details, tid))

            msg = "record successfully updated"
        except:
            msg = "can't be updated"
        finally:
            return redirect(url_for('view'))
            con.close()
    else:
        return "No updation process occured"
