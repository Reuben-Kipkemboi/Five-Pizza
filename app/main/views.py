from unicodedata import category
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
        category = form.category.data 
        new_pizza = Pizza(pizza_type = pizza_type,pizza_price=pizza_price,description=description, category = category)
        
        new_pizza.save_pizza()
        return redirect(url_for('main.pizza_display'))

    else:
        all_pizzas = Pizza.query.all

    return render_template('user.html', form = form, pizzas=all_pizzas)

@main.route('/pizza', methods = ['GET', 'POST'])
# @login_required
def pizza_display():
    '''
    View page for the pitches created with their data
    '''

    # pitches= Pitch.get_pitches
    pizzas = Pizza.query.all()
    


    return render_template('pitches.html', pizzas= pizzas)