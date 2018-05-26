# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:25:08 2018

@author: tperiyas
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'