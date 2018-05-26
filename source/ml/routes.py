# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:59:42 2018

@author: tperiyas
"""

from flask import render_template
from app import app
from app.forms import LoginForm

# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
if __name__ == '__main__':
   app.run(debug = True)