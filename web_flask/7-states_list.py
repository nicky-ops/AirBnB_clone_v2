#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask, render template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    '''
    render states_list html page to diplay created States'
    '''
    states = storage.all()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
