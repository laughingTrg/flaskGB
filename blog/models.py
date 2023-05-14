from flask_login import UserMixin
from .app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<User %r>' % (self.email)
