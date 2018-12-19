from src import dbconnect as sql
# from collections import namedtuple - TBD


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
    # return username, password
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT UserName, Pass FROM Users WHERE UserName = '" + username + "' AND Pass = '" + password + "'")
    user = cur.fetchone()
    conn.close()
    return user


def check_code(username: str, code: str) -> bool:
    """
    checking if code got from form is as code in DB
    FIXME remove return when everything will be OK
    """
    return True
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT Code FROM Users WHERE UserName = '" + username + "'")
    dbcode = cur.fetchone()
    conn.close()
    if code == dbcode:
        return code == dbcode
    else:
        return code == dbcode


def is_admin(username: str) -> bool:
    """
    checking if user is admin
    FIXME remove return when everything will be OK
    """
   # return True
    conn = sql.connect()
    cur = conn.cursor()
    cur.execute("SELECT Role FROM Users WHERE UserName = '" + username + "'")
    role = cur.fetchone()
    conn.close()
    if role == 'admin':
        return True
    else:
        return False


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
