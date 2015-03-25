#!/usr/bin/env python

import sys

from flask import Flask
from flask import request

from raspipe import RasPipe

app = Flask(__name__)

rp = RasPipe(None)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/display', methods=['POST'])
def display():
    rp.input_lines.append(request.form['line'])
    rp.render_frame()
    return request.form['line']

@app.route('/quit')
def quit():
    sys.exit()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

