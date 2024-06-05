from app import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(500), nullable=False, default='https://beforeigosolutions.com/wp-content/uploads/2021/12/dummy-profile-pic-300x300-1.png')
    password = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f'User: {self.username}, Email: {self.email}'