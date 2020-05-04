from flask import Flask, render_template

from .models import database, Video

app = Flask(__name__)

# Middlewares
@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response

# Request
@app.route('/')
def index():
    return render_template('index.html')