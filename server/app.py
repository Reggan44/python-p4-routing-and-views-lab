#!/usr/bin/env python3

from flask import Flask
from flask import request
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

# Count route
@app.route('/count/<int:param>')
def count(param):
    return '\n'.join(str(i) for i in range(param)) + '\n'

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    return str(result)
