from app import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False, default="")
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(500), nullable=False, default='default.jpg')
    phone_number = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    schedule = db.relationship('Scheduling', backref='customer', lazy=True)


    def __repr__(self):
        return f'User: {self.first_name}, Email: {self.email}' 
class Scheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'Scheduling: {self.date}, Type: {self.type}'