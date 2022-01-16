from doctest import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():  # called routes or views usually
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template('market.html', item_names='Phone')


''' 
@app.route('/about/<username>')  # dynamic address
def about_page(username):
    # bad, but functionall way to return html content
    return f"<h1>This is {username} page</h1>"
'''

app.run(debug=True)
# alternatively run it through console
# set F  FLASK_DEBUG=1
