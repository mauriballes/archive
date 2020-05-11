import functools
import os

from flask import Flask, render_template, request, g, session, redirect, url_for, flash
from playhouse.shortcuts import model_to_dict
from werkzeug.security import check_password_hash

from .models import database, User, Video

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'my-secret-key')


"""
Middlewares
"""
@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response

def login_required(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return inner


"""
Auth
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.select().where(User.username == username).first()
        error = None

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."
            
        if error is None:
            session.clear()
            session['user'] = model_to_dict(user)
            return redirect(url_for('index'))

        flash(error)
        
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))


"""
Routes
"""
@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html')