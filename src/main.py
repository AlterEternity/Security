import logging
from functools import partial
from logging import getLogger
from flask import Flask
from flask import render_template
# render_template_string
from flask import request
from flask import redirect, url_for, session
from flask.views import MethodView

from src import models as dbhandler

app = Flask(__name__)
app.secret_key = 'SuperSecretRandomString(YouReLaughing,ButGoodSemanticPasswordsRule)'

# init logger
logger = getLogger('__main__')
# create logger with 'spam_application'
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
all_handler = logging.FileHandler('all.log')
all_handler.setLevel(logging.DEBUG)
# create console handler with a higher log level
crit_handler = logging.FileHandler('crit.log')
crit_handler.setLevel(logging.WARNING)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
all_handler.setFormatter(formatter)
crit_handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(all_handler)
logger.addHandler(crit_handler)


def get_logs(path):
    with open(path, 'r') as out:
        raw_data = out.readlines()
    data = []
    events = len(raw_data)
    for line in raw_data:
        data.append(line.split())
    return data


get_all_logs = partial(get_logs, 'all.log')
get_crit_logs = partial(get_logs, 'crit.log')


def current_user():
    return session.get('username', '')


def set_current_user(username):
    session['username'] = username


class LoginView(MethodView):
    methods = ['GET', 'POST']
    template_name = './index.html'

    def get(self):
        return render_template(self.template_name)

    def post(self):
        """
        login logic
        route for method POST (when form submitted)
        """
        code = request.form.get('captcha-code')
        username = request.form.get('username')
        password = request.form.get('password')
        # creating dictionary for following logic
        ctx = {'captcha': True, 'username': username}

        # captcha inserted/not inserted
        if code:
            logger.info(f'User {username} logged in, step 2')
            # FIXME Remove False after function check_code is created
            # captcha valid/invalid
            if dbhandler.check_code(ctx['username'], code):
                logger.info(f'User {username} successfully logged in')
                set_current_user(username)
                return redirect(url_for('index'), 200)
            else:
                logger.warning(f'User {username} posted wrong captcha')
                return render_template(self.template_name, error='Incorrect captcha code', **ctx)

        # user valid/non valid
        user = dbhandler.search_user(username, password)
        if user:
            logger.info(f'User {username} logged in, step 1')
            return render_template(self.template_name, **ctx)

        logger.warning(f'User {username} posted wrong password')
        return render_template(self.template_name, error='Incorrect username or password')


@app.route('/home/', methods=['GET'])
def index():
    """
    route for redirecting
    TODO create page for redirecting
    """
    is_admin = dbhandler.is_admin(current_user())
    return render_template('./welcome.html', username=current_user(), is_admin=is_admin)


app.add_url_rule('/', view_func=LoginView.as_view('login'))


@app.route('/admin/', methods=['POST'])
def admin():
    """
    route for redirecting
    """
    with open('all.log', 'r') as out:
        raw_data = out.readlines()
    all_logs = []
    events_all = len(raw_data)
    for line in raw_data:
        all_logs.append(line.split())

    with open('crit.log', 'r') as out:
        crit_data = out.readlines()
    crit_logs = []
    events_crit = len(crit_data)
    for line in crit_data:
        crit_logs.append(line.split())
    return render_template('./admin.html', events_all=events_all, events_crit=events_crit, all_logs=all_logs,
                           crit_logs=crit_logs)


def staff_only(func):
    def inner(user):
        if dbhandler.is_admin(user):
            return func
        raise ValueError('You cannot view this page')
    return inner


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
