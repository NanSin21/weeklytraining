from flask import *
import sqlite3
app = Flask(__name__,template_folder='template')  
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login',methods = ['POST','GET'])  
def login():
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
                msg = "Intern successfully Added"
        except:
            con.rollback()
            msg = "We can not add the intern to the list"
        finally:
            return render_template("about.html",msg = msg)
            con.close()
    else:
        return render_template('login.html')

@app.route('/details')
def details():
    con = sqlite3.connect("todo.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Interns")  
    rows = cur.fetchall()
    print(rows,'rows')  
    return render_template("details.html",rows = rows) 

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
                return redirect(url_for('details'))
    else:
        return "No deletion process occured"

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
            return redirect(url_for('details'))
    else:
        return "No updation process occured"

@app.route('/task', methods=['POST','GET'])
def task():
    msg="msg"
    if request.method=="POST":
        try:
            todo=request.form['todo']
            datime=request.form['datet']
            details=request.form['descrip']
            #print(todo,datime,details,'dadadadadata')
            with sqlite3.connect("todo.db") as con:
                cur = con.cursor()
                print(todo,'todo')
                cur.execute("INSERT into Tasks (todo, datime, details) values (?,?,?)",(todo,datime,details))
                con.commit()
                msg = "Task successfully Added"
                print(msg,'msg')
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
    print(rows)  
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
    app.debug = True
    app.run()
