# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:20:21 2018

@author: tperiyas
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'login.html'

if __name__ == '__main__':
    app.run()
