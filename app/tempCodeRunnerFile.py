class Scheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)