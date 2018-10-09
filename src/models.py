# TODO Create models. Adding/deleting users. Deadline - 6.10.2018. Done
import dbconnect as sql


# for future - make signup implementation
def addUser(username, password):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (UserName,Pass) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


# prototype for user verification
def searchUser(username, password):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Pass WHERE UserName = '(?)' AND Pass = '(?)'", (username, password))
    user = cur.fetchone()
    return user


# getting list of registered users
def getUsers():
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Pass FROM Users")
    users = cur.fetchall()
    conn.close()
    return users
