# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:13:28 2020

@author: Dhanush
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
from script import scrap
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():

    field=request.form['Field']
    Experience=request.form['Experience']
    Location=request.form['Location']
    output=scrap(field=field,Experience=Experience,Location=Location)
    
    return output
if __name__ == "__main__":
    app.run(debug=True)