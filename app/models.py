from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(500), unique=True, nullable=False, default='https://beforeigosolutions.com/wp-content/uploads/2021/12/dummy-profile-pic-300x300-1.png')
    password = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f'User: {self.username}, Email: {self.email}'