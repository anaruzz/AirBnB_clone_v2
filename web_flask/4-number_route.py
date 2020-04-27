#!/usr/bin/python3
"""
Script that starts a flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>')
def py_route(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_number(n):
    if type(n) is int:
        return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
