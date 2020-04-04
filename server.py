# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:35:54 2020

@author: elifaskvav
"""

#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
import requests as rs
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
from flask_cors import CORS, cross_origin
# https://pypi.python.org/pypi/Flask-Cors

# https://pythonspot.com/mysql-with-python/
import MySQLdb
import json
#from bson import json_util


app = Flask(__name__)
#running command in windows
# export FLASK_APP=hello
# flask run




# Run with:
# FLASK_APP=server.py flask run

# http://flask.pocoo.org/docs/0.12/api/#flask.request
from flask import Flask,request

# https://pypi.python.org/pypi/Flask-Cors
from flask_cors import CORS, cross_origin

# https://pythonspot.com/mysql-with-python/
import MySQLdb
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route("/api/leases",methods=['GET'])
def getLeases():

    db = MySQLdb.connect(host="localhost",  # your host 
                         user="root",       # username
                         passwd="toor",     # password
                         db="dhcpserver")   # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # Select data from table using SQL query.
    cur.execute("SELECT * FROM dhcpclients")

    rows = cur.fetchall()
    row_headers=[x[0] for x in cur.description] #this will extract row headers

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data,indent=4, sort_keys=True, default=str)
#json.dumps(anObject, default=json_util.default)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

 
if __name__ == '__main__':
    cors = CORS(app,resources={r"*": {"origins": "*"}},allow_headers="*")
    # app.run(host='0.0.0.0',port=5000,ssl_context='adhoc')#app.run(debug=True)#!flask/bin/python





