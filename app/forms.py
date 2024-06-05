from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, IntegerField

from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

class Registration(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email =  StringField('Email',
                          validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')




class LoginForm(FlaskForm):

    email =  StringField('Email',
                          validators=[DataRequired(), Email() ])

    password = PasswordField('Passwordd',
                             validators=[DataRequired()])
    
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign Up')


class Recycling(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField('Type', choices=[('plastic', 'Plastic'), ('paper', 'Paper'), ('metal', 'Metal'), ('glass', 'Glass'), ('all', 'All')], validators=[DataRequired()])
    amount = IntegerField('Amount (in kg)', validators=[DataRequired(), NumberRange(min=1)], render_kw={"placeholder": "Enter amount in kg"})
    submit = SubmitField('Submit')

class Scheduling(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField('Type', choices=[('plastic', 'Plastic'), ('paper', 'Paper'), ('metal', 'Metal'), ('glass', 'Glass'), ('all', 'All')], validators=[DataRequired()])
    submit = SubmitField('Submit')

