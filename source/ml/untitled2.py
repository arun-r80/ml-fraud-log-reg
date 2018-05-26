# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:14:36 2018

@author: tperiyas
"""

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})