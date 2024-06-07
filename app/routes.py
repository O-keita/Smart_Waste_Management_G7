import os
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from app.forms import Registration, LoginForm, Recycling, Scheduling, updateAccount
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
        user = User(first_name=form.first_name.data,
                    middle_name =form.middle_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data, password=hashed_password,
                    sex=form.sex.data, address=form.address.data, 
                    house_number=form.house_number.data, 
                    location=form.location.data, 
                    phone_number=form.phone_number.data, 
                    )
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.first_name.data}', 'success')

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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = updateAccount()

    img_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

     

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
 
        
    
    return render_template('account.html', img_file=img_file, form=form)


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