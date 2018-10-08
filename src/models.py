# TODO Create models. Adding/deleting users. Deadline - 6.10.2018. Done
import dbconnect as sql

def addUser(username,password):
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (username,password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def getUsers():
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Password FROM Users")
    users = cur.fetchall()
    conn.close()
    return users












