from flask import render_template, flash, redirect, url_for
from app.forms import Registration, LoginForm, Recycling, Scheduling
from app.models import User
from app import app
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        flash('Succefully Logged In', 'success')
        

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = Registration()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', 'success')

        return redirect(url_for('home'))

    return render_template('register.html', form=form)

@app.route('/recycle', methods=['GET', 'POST'])
def recycle():

    form = Recycling()

    return render_template('recycle.html', form=form)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():

    form = Scheduling()

    return render_template('schedule.html', form=form)
