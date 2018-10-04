import pyodbc

# connection parameters

server = 'servername'
port = '1433'
db = 'dbname'
username = 'user'
pwd = 'pwd'
driver = '{ODBC Driver 13 for SQL Server}'

# create connection to db
sqlconn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=' + port + ';DATABASE=' + db + ';UID='
                         + username + ';PWD=' + pwd)

# TODO Fill all parameters. Deadline - 6.10.2018

# init cursor
cursor = sqlconn.cursor()

# test connection
cursor.execute("sql query")
row = cursor.fetchone()

# output table
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
