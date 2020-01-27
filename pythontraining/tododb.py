import sqlite3  
  
con = sqlite3.connect("todo.db")  
print("Database opened successfully")  
  
con.execute("create table Interns (uid INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL, psw TEXT UNIQUE NOT NULL)")  
print("Table interns created successfully")
con.execute("create table Tasks (tid INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT NOT NULL, datime TEXT NOT NULL, details TEXT NOT NULL, uid INTEGER NOT NULL, FOREIGN KEY (uid) REFERENCES Interns (uid) )")  
print("Table tasks created successfully")
con.execute("create table Admins (aid INTEGER PRIMARY KEY AUTOINCREMENT, aname TEXT NOT NULL, admail TEXT UNIQUE NOT NULL, adpsw TEXT UNIQUE NOT NULL)")
print("Table admins created successfully")
con.close() 