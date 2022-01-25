from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():  # called routes or views usually
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)


''' 
@app.route('/about/<username>')  # dynamic address
def about_page(username):
    # bad, but functionall way to return html content
    return f"<h1>This is {username} page</h1>"
'''
