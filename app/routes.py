""" routes.py acts as a controller for incoming requests and yields rendered html templates """

from flask import flash, redirect, request, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from outpost_calc import (convert_cards_str_to_nums,
                          find_unique_totals,
                          find_unused_cards_totals,
                          sort_by_totals)
from app import app
from app.forms import LoginForm, CardsForm
from app.models import User

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    """ The main page of the site: enter a deck of cards and see totals """
    form = CardsForm()
    totals = None
    if form.validate_on_submit():
        # TODO: refactor the interface to outpost_calc ... individual functions
        # make for easy unit testing, but this usage feels lumpy
        cards_num = convert_cards_str_to_nums(form.cards.data)
        totals = find_unique_totals(cards_num)
        totals = find_unused_cards_totals(cards_num, totals)
        totals = sort_by_totals(totals)

    return render_template('index.html', title='Home', form=form, totals=totals)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Typical login page """
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
    """ Typical logout function """
    logout_user()
    return redirect(url_for('index'))

@app.route('/about')
@login_required
def about():
    """ An About page that explains this app """
    return render_template('about.html', title='About')
