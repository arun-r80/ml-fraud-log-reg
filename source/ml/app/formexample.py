# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:21:08 2018

@author: tperiyas
"""

from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
#app = Flask(__name__, template_folder='templates')
#app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   print('Hai')
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('contact.html')
      #elif request.method == 'GET':
       #  return render_template('contact.html', form = form)

if __name__ == '__main__':
   
   app.run(debug = True)