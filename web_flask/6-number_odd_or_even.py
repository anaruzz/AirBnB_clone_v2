#!/usr/bin/python3
"""
Script that starts a flask web application
"""
from flask import Flask, render_template

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
def number(n):
    if type(n) is int:
        return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if type(n) is int:
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', n=n, val='even')
        else:
            return render_template('6-number_odd_or_even.html', n=n, val='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
