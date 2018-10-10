# TODO Create models. Adding/deleting users. Deadline - 6.10.2018. Done
from src import dbconnect as sql
# from collections import namedtuple - TBD

weak_passwords = ['12345678',
                  'qwertyui',
                  'qwerty123']


def add_user(username: str, password: str) -> None:
    """
    For future - make signup implementation
    """
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (UserName,Pass) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def search_user(username: str, password: str) -> tuple or None:
    """
    Prototype for user verification
    """
    # FIXME Remove when web is ok
    return username, password
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Pass WHERE UserName = '(?)' AND Pass = '(?)'", (username, password))
    user = cur.fetchone()
    conn.close()
    return user


def get_users() -> list:
    """
    Getting list of registered users
    """
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Pass FROM Users")
    users = cur.fetchall()
    conn.close()
    return users
