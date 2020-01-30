from flask import *
import sqlite3
from flask_paginate import Pagination, get_page_args
import os

admin = Blueprint('admin', __name__, template_folder='template')

users = list(range(100))


def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]

############ Admin Panel Search Page ###########
@admin.route('/adminsearch', methods=['POST', 'GET'])
def adminsearch():
    if 'aname' in session:
        username = session['aname']
        keyword = str(request.args.get('vocab'))

        con = sqlite3.connect("todo.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select Interns.uname,Tasks.todo,Tasks.details from Tasks LEFT JOIN Interns ON Tasks.uid=Interns.uid where Tasks.todo LIKE '%" +
                    keyword+"%' or Tasks.details LIKE '%"+keyword+"%'")
        rows = cur.fetchall()

        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_users = get_users(offset=offset, per_page=10)
        pagination = Pagination(page=page, per_page=10,
                                total=total, css_framework='bootstrap4')

        return render_template("/admin/adminsearch.html", username=username, users=pagination_users, page=page, per_page=per_page, pagination=pagination, rows=rows, total=total)
        con.close()

############ User Details Page ###########
@admin.route('/details', methods=['POST', 'GET'])
def details():
    con = sqlite3.connect("todo.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select Interns.uid,Interns.uname,Interns.email,Interns.address,count(Tasks.tid) from Interns LEFT JOIN Tasks ON Interns.uid=Tasks.uid GROUP BY Interns.uid ORDER BY COUNT(Tasks.uid) DESC")
    #cur.execute("select * from Interns")
    rows = cur.fetchall()

    return render_template("/admin/details.html", rows=rows)
    con.close()

############ Admin adding user ###########
@admin.route('/adduser', methods=['POST', 'GET'])
def adduser():
    msg = "msg"
    if request.method == "POST":
        uname = request.form['uname']
        email = request.form['email']
        address = request.form['address']
        password = request.form['psw']
        try:
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("INSERT into Interns (uname, email, address, psw) values (?,?,?,?)",
                        (uname, email, address, password))

            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return redirect(url_for("details"))
            con.close()
    else:
        return "no remove"
