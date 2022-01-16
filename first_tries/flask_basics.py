from doctest import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():  # called routes or views usually
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


''' 
@app.route('/about/<username>')  # dynamic address
def about_page(username):
    # bad, but functionall way to return html content
    return f"<h1>This is {username} page</h1>"
'''

app.run(debug=True)
# alternatively run it through console
# set F  FLASK_DEBUG=1
