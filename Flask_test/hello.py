# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:59:51 2016

@author: jmtaysom
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
