from app import db, login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  nullable= False, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False, default="")
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False,)
    sex = db.Column(db.String(50), nullable=False, default='Male')
    address = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(500), nullable=False, default='default.jpg')
    phone_number = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    schedule = db.relationship('Scheduling', backref='customer', lazy=True)


    def __repr__(self):
        return f'User: {self.first_name}, Email: {self.email}' 
class Scheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'Scheduling: {self.date}, Type: {self.type}'
    
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scheduling, db.session))