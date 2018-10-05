import pyodbc

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

# TODO Fill all parameters. Deadline - 6.10.2018 - DONE

# init cursor
cursor = sqlconn.cursor()

# test connection
cursor.execute("Query")
row = cursor.fetchone()

# output table
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
