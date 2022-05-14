from flask import render_template
from . import auth

@auth.route('/user-login')
def userlogin():
    return render_template('auth/login.html')