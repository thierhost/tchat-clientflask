#/usr/bin/env python 2.7
# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,url_for,render_template
import os


app=Flask(__name__)

#definition des routes
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/discussions')
def discussions():
	return render_template("discussions.html")


app.run(debug= True)
	