from ..import db
from flask import render_template,redirect, url_for, flash
from . import main
from ..models import User, Pizza,Toppings
from .forms import PizzaForm
# from .. import db,photos
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import current_user, login_required

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/toppings')
def toppings():
    
    return render_template('toppings.html')


@main.route('/pizza')
def pizza():
    
    return render_template('another.html')


@main.route('/menu')
def menu():
    
    return render_template('another.html')

@main.route('/add_new', methods =['POST','GET'])
# @login_required
def new_pizza():

    form = PizzaForm() 
    if form.validate_on_submit():
        pizza_type = form.name.data
        pizza_price = form.price.data
        description = form.description.data
        user_id = current_user
        pizza_size = form.category.data 
        new_pizza_object = Pizza(pizza_type = pizza_type,pizza_price=pizza_price,description=description, pizza_size=pizza_size)
        db.session.add(new_pizza_object )
        db.session.commit()
        # new_pizza_object.save_p()
        print("new pizza",new_pizza_object)
        # return redirect(url_for('main.index')) 
    
       
    return render_template('user.html', form = form)