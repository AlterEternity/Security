import pyodbc


# connection to db
def connect():
    # connection parameters
    server = 'kpi-7-security.database.windows.net'
    port = '1433'
    db = 'Security'
    username = 'dladmin'
    pwd = 'Velkomm1'
    driver = '{ODBC Driver 13 for SQL Server}'

    # create connection to db
    sqlconn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=' + port + ';DATABASE=' + db + ';UID='
                             + username + ';PWD=' + pwd)

    # returning connection variable
    return sqlconn

