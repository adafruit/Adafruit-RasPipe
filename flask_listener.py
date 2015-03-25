#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for

from raspipe import RasPipe

app = Flask(__name__)

rp = RasPipe(None)
rp.input_lines.append('starting up...')
rp.render_frame()

@app.route('/')
def index():
    return render_template('index.html', rp=rp)

@app.route('/display', methods=['POST'])
def display():
    rp.input_lines.append(request.form['line'])
    rp.render_frame()
    return redirect(url_for('index'))

@app.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return "Quitting..."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
