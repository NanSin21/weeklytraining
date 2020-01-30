from flask import *
import sqlite3
import os

auth = Blueprint('auth', __name__, template_folder='template')

############ Admin Login Page ###########
@auth.route('/adminsignup', methods=['POST', 'GET'])
def adminsignup():
    msg = "msg"
    if request.method == "POST":
        try:
            aname = request.form['aname']
            admail = request.form['admail']
            adpassword = request.form['adpsw']
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("INSERT into Admins (aname, admail, adpsw) values (?,?,?)",
                        (aname, admail, adpassword))
            con.commit()
        except:
            con.rollback()
            msg = "We can not add the admin to the list"
        finally:
            return render_template("/admin/admin.html", msg=msg)
            con.close()
    else:
        return render_template('/admin/admin.html')

############ User Signup Page ###########
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    msg = "msg"
    if request.method == "POST":
        try:
            uname = request.form['uname']
            email = request.form['email']
            address = request.form['address']
            password = request.form['psw']
            con = sqlite3.connect("todo.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("INSERT into Interns (uname, email, address, psw) values (?,?,?,?)",
                        (uname, email, address, password))
            con.commit()
            msg = "Intern successfully Added"
        except:
            con.rollback()
            msg = "We can not add the intern to the list"

        finally:
            return render_template('/authentication/signup.html', msg=msg)
            con.close()
    else:

        return render_template('/authentication/signup.html')

############ Admin Login Page ###########
@auth.route('/adminlogin', methods=['POST', 'GET'])
def adminlogin():
    error = None
    """ if 'aname' in session:
        return redirect(url_for('about')) """
    if request.method == 'POST':
        username_form = request.form['aname']
        password_form = request.form['adpsw']
        con = sqlite3.connect("todo.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT COUNT(1) FROM Admins WHERE aname = ?;",
                    [username_form])  # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT adpsw FROM Admins WHERE aname = ?;", [
                        username_form])  # FETCH THE PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['aname'] = request.form['aname']
                    return redirect(url_for('details'))
                else:
                    error = "Invalid Credential"
        else:
            error = "Invalid Credential"
        return render_template('/admin/adminlogin.html', error=error)
        con.close()
    else:
        return render_template('/admin/adminlogin.html')

############ User Login Page ###########
@auth.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    """ if 'uname' in session:
        return redirect(url_for('about')) """

    if request.method == 'POST':
        username_form = request.form['uname']
        password_form = request.form['psw']
        con = sqlite3.connect("todo.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT COUNT(1) FROM Interns WHERE uname = ?;", [
                    username_form])  # CHECKS IF USERNAME EXIST
        if cur.fetchone()[0]:
            cur.execute("SELECT psw FROM Interns WHERE uname = ?;",
                        [username_form])  # FETCH THE PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['uname'] = request.form['uname']
                    username = session['uname']
                    return redirect(url_for("about"))
                else:
                    error = "Invalid Credential"
        else:
            error = "Invalid Credential"
        return render_template('/authentication/login.html', error=error)
        con.close()
    else:
        return render_template('/authentication/login.html')

############ Logout Page ###########
@auth.route("/logout")
def logout():
    if 'uname' in session:
        username = session['uname']
    if 'aname' in session:
        username = session['aname']
    session.pop(username, None)
    return render_template('home.html')
