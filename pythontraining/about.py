from flask import *
#import mysql.connector

import sqlite3
import os

app = Flask(__name__,template_folder='template') 

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
        return render_template('about.html',username=username)
        
    if 'uname' in session:
        username = session['uname']
        return render_template('about.html',username=username)
        
    else:
        return redirect(url_for('home'))
   


@app.route('/adminsignup',methods = ['POST','GET'])
def adminsignup():
    msg="msg"
    if request.method=="POST":
        try:
            aname=request.form['aname']
            admail=request.form['admail']
            adpassword=request.form['adpsw']
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Admins (aname, admail, adpsw) values (?,?,?)",(aname,admail,adpassword))
                con.commit()
        except:
            con.rollback()
            msg = "We can not add the admin to the list"
        finally:
            return redirect(url_for("details"))
            con.close() 
    else:
        return render_template('admin.html')

@app.route('/adminlogin',methods = ['POST','GET'])
def adminlogin():
    error = None
    """ if 'aname' in session:
        return redirect(url_for('about')) """
    if request.method == 'POST':
        username_form  = request.form['aname']
        password_form  = request.form['adpsw']
        con = sqlite3.connect("todo.db")  
        con.row_factory = sqlite3.Row 
        cur = con.cursor()
        cur.execute("SELECT COUNT(1) FROM Admins WHERE aname = ?;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT adpsw FROM Admins WHERE aname = ?;", [username_form]) # FETCH THE PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['aname'] = request.form['aname']
                    return redirect(url_for('details'))
                else:
                    error = "Invalid Credential"
        else:
            error = "Invalid Credential"
        return render_template('adminlogin.html', error=error)
        con.close()
    else:
        return render_template('adminlogin.html')
    
@app.route

@app.route('/signup',methods = ['POST','GET'])  
def signup():
    msg="msg"
    if request.method=="POST":
        try:
            uname=request.form['uname']
            email=request.form['email']
            address=request.form['address']
            password=request.form['psw']
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Interns (uname, email, address, psw) values (?,?,?,?)",(uname,email,address,password))
                con.commit()
                session['logged_in']=True
                msg = "Intern successfully Added" 
        except:
            con.rollback()
            msg = "We can not add the intern to the list"
            
        finally:
            return redirect(url_for("about"))
            con.close()
    else:
        
        return render_template('signup.html')

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    """ if 'uname' in session:
        return redirect(url_for('about')) """
    
    if request.method == 'POST':
        username_form  = request.form['uname']
        password_form  = request.form['psw']
        con = sqlite3.connect("todo.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()
        cur.execute("SELECT COUNT(1) FROM Interns WHERE uname = ?;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT psw FROM Interns WHERE uname = ?;", [username_form]) # FETCH THE PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['uname'] = request.form['uname']
                    username = session['uname']
                    return redirect(url_for("about"))
                else:
                    error = "Invalid Credential"
        else:
            error = "Invalid Credential"
        return render_template('login.html', error=error)
        con.close()
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    if 'uname' in session:
        username=session['uname']
    if 'aname' in session:
        username = session['aname']
    session.pop(username, None)
    return render_template('home.html')

@app.route('/details', methods=['POST','GET'])
def details():
    con = sqlite3.connect("todo.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select Interns.uid,Interns.uname,Interns.email,Interns.address,count(Tasks.tid) from Interns LEFT JOIN tasks ON Interns.uid=Tasks.uid GROUP BY Interns.uid ORDER BY COUNT(Tasks.uid) DESC")
    #cur.execute("select * from Interns")  
    rows = cur.fetchall()
    return render_template("details.html",rows = rows) 

@app.route('/adduser', methods=['POST','GET'])
def adduser():
    msg="msg"
    if request.method=="POST":
        uname=request.form['uname']
        email=request.form['email']
        address=request.form['address']
        password=request.form['psw'] 
        with sqlite3.connect("todo.db") as con:  
            try:  
                cur = con.cursor()  
                cur.execute("INSERT into Interns (uname, email, address, psw) values (?,?,?,?)",(uname,email,address,password)) 
                msg = "record successfully deleted"  
            except:  
                msg = "can't be deleted"  
            finally:  
                return redirect(url_for("details"))
    else:
        return "no remove"

@app.route("/remove",methods = ["POST"])  
def remove():
    msg="msg"
    if request.method=="POST":
        uid = request.form["uid"]  
        with sqlite3.connect("todo.db") as con:  
            try:  
                cur = con.cursor()  
                cur.execute("delete from Interns where uid = ?",uid) 
                msg = "record successfully deleted"  
            except:  
                msg = "can't be deleted"  
            finally:  
                return render_template(url_for('details'), msg)
    else:
        return "cannot remove user"

@app.route('/edit',methods = ["POST"])
def edit():
    if request.method=="POST":
        uid=request.form["uid"]
        try:
            uname=request.form['uname']
            email=request.form['email']
            address=request.form['address']
            password=request.form['psw']
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()  
                cur.execute("update Interns set uname=?, email=?, address=?, psw=?  where uid = ?",(uname,email,address,password,uid)) 
                msg = "Intern record successfully updated"  
        except:  
            msg = "Intern can't be updated"  
        finally:  
            return render_template(url_for('details'),msg)
    else:
        return msg

@app.route('/task', methods=['POST','GET'])
def task():
    msg="msg"
    if request.method=="POST":
        if 'uname' in session:
            username=session['uname']
        try:
            todo=request.form['todo']
            datime=request.form['datet']
            details=request.form['descrip']
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()
                cur.execute("SELECT COUNT(1) FROM Interns WHERE uname = ?;", [username]) # CHECKS IF USERNAME EXSIST
                if cur.fetchone()[0]:
                    cur.execute("SELECT uid FROM Interns WHERE uname = ?;", [username]) # FETCH THE uid
                for row in cur.fetchall():
                    uid=row[0]
                    print(uid)
                cur.execute("INSERT into Tasks (todo, datime, details,uid) values (?,?,?,?)",(todo,datime,details,uid))
                con.commit()
                msg = "Task successfully Added" 
        except:
            con.rollback()
            msg = "We can not add the tasks to the list"
        finally:
            return render_template("task.html",msg = msg)
            con.close()
    else:
        return render_template('task.html')

@app.route("/view")  
def view():  
    con = sqlite3.connect("todo.db")  
    con.row_factory = sqlite3.Row   
    cur = con.cursor()  
    cur.execute("select * from Tasks")  
    rows = cur.fetchall() 
    return render_template("todo.html",rows = rows) 

@app.route("/delete",methods = ["POST"])  
def delete():
    
    msg="msg"
    if request.method=="POST":
        tid = request.form["tid"]  
        with sqlite3.connect("todo.db") as con:  
            try:  
                cur = con.cursor()  
                cur.execute("delete from Tasks where tid = ?",tid) 
                msg = "record successfully deleted"  
            except:  
                msg = "can't be deleted"  
            finally:  
                return redirect(url_for('view')) 
    else:
        return "No deletion process occured"

@app.route('/update',methods = ["POST"])
def update():
    
    if request.method=="POST":
        tid=request.form["tid"]
        try:
            todo=request.form['todo']
            datime=request.form['datet']
            details=request.form['descrip'] 
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()  
                cur.execute("update Tasks set todo=?, datime=?, details=?  where tid = ?",(todo,datime,details,tid)) 
                msg = "record successfully updated"   
        except:  
            msg = "can't be updated"  
        finally:  
            return redirect(url_for('view'))
    else:
        return "No updation process occured"


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
