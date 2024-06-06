from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, IntegerField

from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
from app.models import User
from flask_login import current_user
class Registration(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email',
                          validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username already in use.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already in use.')






class LoginForm(FlaskForm):

    email =  StringField('Email',
                          validators=[DataRequired(), Email() ],  render_kw={'class': 'mt-1 block w-full p-4 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 focus:outline-none'})

    password = PasswordField('Passwordd',
                             validators=[DataRequired()],  render_kw={'class': 'mt-1 block w-full p-4 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 focus:outline-none'})
    
    remember = BooleanField("Remember Me",  render_kw={'class': 'mt-1 block w-full p-4 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 focus:outline-none'})
    submit = SubmitField('Sign Up', render_kw={'class':"w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"})


class Recycling(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField('Type', choices=[('plastic', 'Plastic'), ('paper', 'Paper'), ('metal', 'Metal'), ('glass', 'Glass'), ('all', 'All')], validators=[DataRequired()])
    amount = IntegerField('Amount (in kg)', validators=[DataRequired(), NumberRange(min=1)], render_kw={"placeholder": "Enter amount in kg"})
    submit = SubmitField('Submit')

class Scheduling(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField('Type', choices=[('plastic', 'Plastic'), ('paper', 'Paper'), ('metal', 'Metal'), ('glass', 'Glass'), ('all', 'All')], validators=[DataRequired()])
    submit = SubmitField('Create Schedule')

class updateAccount(FlaskForm):

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email',
                          validators=[DataRequired(), Email()])

    submit = SubmitField('Update')

    def validate_username(self, username):

        if username.data != current_user.username:


            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('Username already in use.')

    def validate_email(self, email):

        if email.data != current_user.email:


            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email already in use.')
      