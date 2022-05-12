from datetime import datetime
from flask_login import UserMixin
from . import db, login_manager

#securing user passwords
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Users table

class User( UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(255))
    useremail = db.Column(db.String(255),unique = True, index = True)
    password_secure = db.Column(db.String(255))
    pizza = db.relationship('Pizza', backref='user', lazy='dynamic')
    toppings = db.relationship('Toppings', backref='user', lazy='dynamic')
    
    #used to create a write only class property password
    @property
    def password(self):
        raise AttributeError('You are not allowed to read passcode')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'