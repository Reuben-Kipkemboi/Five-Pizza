from flask import render_template,redirect, url_for, flash
from . import main
from ..models import User, Pizza,Toppings
from .forms import PizzaForm
# from .. import db,photos
# we want to access the login functionality for some features eg voting and making a pitch
from flask_login import login_required

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

@main.route('/add_new')
def addnew():
    
    return render_template('user.html')

# @main.route('/create_new', methods =['POST','GET'])
# @login_required
# def new_pitch():
#     form = PitchesForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         pitchcontent = form.content.data
#         category = form.category.data
#         user_id = current_user
#         new_pitch_object = Pitch( name = name, pitchcontent=pitchcontent,user_id=current_user._get_current_object().id,category=category)
#         new_pitch_object.save_pitch()
#         return redirect(url_for('main.index'))
        
#     return render_template('newpitch.html', form = form)

