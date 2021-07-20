import re
from flask import Flask, request, render_template
from application import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def product():
    return render_template('shop.html')

@app.route('/user')
def user():
    return render_template('user.html')
