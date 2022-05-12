from flask import render_template
from . import main

@main.route('/')
def index():
    
    return render_template('index.html')


@main.route('/user')
def user():
    
    return render_template('user.html')


@main.route('/toppings')
def toppings():
    
    return render_template('toppings.html')


@main.route('/pizza')
def pizza():
    
    return render_template('pizza.html')
