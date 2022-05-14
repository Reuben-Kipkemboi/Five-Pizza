from flask_login import UserMixin
from sqlalchemy import ForeignKey
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
     
#pizza model class 
class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key = True) 
    pizza_type = db.Column(db.String(255))
    pizza_price = db.Column(db.Integer)
    pizza_size = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable = False)
    user_id = db.Column(db.Integer, ForeignKey('users.id')) 
    toppings = db.relationship('Toppings', backref='toppings', lazy='dynamic')

    def save_p(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_pizzas(cls,pizza_size):
        pizzas = Pizza.query.filter_by(pizza_size=pizza_size).all()
        return pizzas

    def __repr__(self):
        return f'Pizza {self.pizza_type}'

#Toppings model   
class Toppings(db.Model):
    __tablename__ = 'toppings'
    id = db.Column(db.Integer, primary_key = True) 
    toppings_type = db.Column(db.String(255))
    toppings_price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, ForeignKey('pizza.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    
