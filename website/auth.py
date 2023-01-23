from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/')
def terminal():
    return render_template('terminal.html')

@auth.route('/sqweeker')
def sqweeker():
    return render_template('sqweeker.html')