#!/usr/bin/python3
"""
THis script starts a flask web application
"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    returns Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    displays HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    display C followed by text
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """
    route to display python is cool
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''
    route to display n if it is an integer
    '''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_route(n=None):
    """
    route to display a html page if n is an integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
