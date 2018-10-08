from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)


# login logic
@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.addUser(username, password)
        users = dbHandler.getUsers()
        return render_template('./index.html', users=users)
    else:
        return render_template('./index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
