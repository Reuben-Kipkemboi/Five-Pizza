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


# @main.route('/user')
# def user():
    
#     return render_template('user.html')


@main.route('/toppings')
def toppings():
    
    return render_template('toppings.html')


@main.route('/pizza')
def pizza():
    
    return render_template('pizza.html')

@main.route('/add_new', methods =['POST','GET'])
# @login_required

def new_pizza():
    all_pizza = Pizza.query.all()
    form = PizzaForm() 
    if form.validate_on_submit():
        pizza_type = form.name.data
        pizza_price = form.price.data
        description = form.description.data
        user_id = current_user
        pizza_size = form.category.data 
        new_pizza_object = Pizza(pizza_type = pizza_type,pizza_price=pizza_price,description=description, pizza_size=pizza_size)
        new_pizza_object.save_p()
        return redirect(url_for('main.index'))    
    return render_template('user.html', form = form, all_pizza=all_pizza)


# @main.route('/create_new',methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = PitchForm()

#     if form.validate_on_submit():
#         category = form.category.data
#         context = form.context.data
#         new_pitch = Pitch(category=category,context=context)
#         #Database save a new pitch
#         new_pitch.save_pitch()
#         return redirect(url_for('main.pitch_display'))
#     else:
#         all_pitches = Pitch.query.order_by(Pitch.posted).all

#     return render_template('n
# return render_template('new_pitch.html',pitch_form = form,pitches=all_pitches)
