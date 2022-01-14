from doctest import debug
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # called routes or views usually
    return "<h1>Hello, World!</h1>"


@app.route('/about/<username>')  # dynamic address
def about_page(username):
    return f"<h1>This is {username} page</h1>"


app.run(debug=True)
# alternatively run it through console
# set F  FLASK_DEBUG=1
