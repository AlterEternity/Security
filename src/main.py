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
logger = getLogger('__main__')


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
        TODO check redesigning based on global variable
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
            if True or dbhandler.check_code(ctx['username'], code):
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
        return render_template(self.template_name, error='Incorrect email or password')


@app.route('/home/', methods=['GET'])
def index():
    """
    route for redirecting
    TODO create page for redirecting
    """
    return render_template('./welcome.html', username=current_user())


app.add_url_rule('/', view_func=LoginView.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
