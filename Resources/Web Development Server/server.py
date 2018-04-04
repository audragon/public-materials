#!/usr/bin/env python3

import webbrowser
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/about/<name>')
@app.route('/about')
def about(name=None):
    if name is None:
        return render_template("about_me_template.html")
<<<<<<< HEAD
    
    return render_template("about_{0}.html".format(name))
=======

    return render_template("about_{0}.html".format(name), user=name)
>>>>>>> c2c64da17af16930fb10b88c500896b79b2c5a29


if __name__ == '__main__':
    webbrowser.open('http://localhost:5000/')
    app.run(host='0.0.0.0', port=5000)
