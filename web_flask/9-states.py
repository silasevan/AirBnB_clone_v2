#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of all states."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=sorted(states, key=lambda s: s.name))

@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays cities for a given state."""
    state = storage.all(State).get('State.' + id)
    if state:
        cities = sorted(state.cities, key=lambda c: c.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', state=None)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
