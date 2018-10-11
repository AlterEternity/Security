from flask import Flask
from flask import render_template
# render_template_string
from flask import request
from flask import redirect, url_for
from src import models as dbhandler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def login_submitted():
    """
        login logic
        route for method POST (when form submitted)
        TODO check redesigning based on global variable
    """
    global username
    code = request.form.get('captcha-code')
    username = request.form.get('username')
    password = request.form.get('password')
    # creating dictionary for following logic
    # TODO do we need it?
    ctx = {'captcha': True, 'username': username}

    # captcha inserted/not inserted
    if code:
        return captcha_validation(code, **ctx)

    # user valid/non valid
    # TODO do we need to use variable username?
    user = dbhandler.search_user(username, password)
    if user:
        print('Logged in, step 1')
        return render_template('./index.html', **ctx)

    return render_template('./index.html', error='Incorrect email or password')


@app.route('/', methods=['GET'])
def login_not_submitted():
    """
       login logic
       route for method GET (when form not submitted)
    """
    return render_template('./index.html')


@app.route('/home/', methods=['GET'])
def index():
    """
        route for redirecting
        TODO create page for redirecting
    """
    return render_template('./welcome.html', username=username)


def captcha_validation(code, **ctx):
    """
        validation of captcha by looking in DB
    """
    print('Logged in, step 2')
    # FIXME Remove False after function check_code is created
    # captcha valid/invalid
    # TODO do we need to use **ctx?
    if False and dbhandler.check_code(ctx['username'], code):
        return redirect(url_for('index'), 200)
    else:
        return render_template('./index.html', error='Incorrect captcha code', **ctx)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
