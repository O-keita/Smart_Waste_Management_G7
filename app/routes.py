from flask import render_template, flash, redirect, url_for
from app.forms import Registration, LoginForm, Recycling, Scheduling
from app.models import User
from app import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        flash('Succefully Logged In', 'success')
        

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.username.data}', 'success')

        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route('/recycle', methods=['GET', 'POST'])
@login_required
def recycle():

    form = Recycling()

    return render_template('recycle.html', form=form)

@app.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():

    form = Scheduling()

    return render_template('schedule.html', form=form)
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    img_file = current_user.image_file
    return render_template('account.html', img_file=img_file)


@app.route('/user_dashboard', methods=['GET', 'POST'])
@login_required
def user_dashboard():

    return render_template('user_dashboard.html')
@app.route('/admin_dashboard', methods=['GET', 'POST'])

@login_required
def admin_dashboard():

    return render_template('admin_dashboard.html')





@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))