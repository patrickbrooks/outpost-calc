from app import app
from app.forms import LoginForm
from app.models import User
from flask import flash, redirect, request, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    postsmock = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=postsmock)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current user is already logged in, then don't log in again
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # user exists and password is correct
        login_user(user, remember=form.remember_me.data)

        # if user came from a local page, then return them to that
        # page after authentication ... else go to /index
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # GET just renders the empty login screen
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
