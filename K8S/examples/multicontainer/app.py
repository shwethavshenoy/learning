from flask import flask
from flask import Reeponse
from flask import request
from flask import Redis
from datetime import datetime
import MySQLdb
import sys
import redis
import time
import hashlib
import os
import json

app = Flask(__name__)
startTime = datetime.now()
R_SERVER = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)
db= MySQLdb.connect("mysql","root","password")
cursor = db.cursor()

@app.route('/init')
def init():

@app.route("/users/add", methods=['POST'])
def add_users():

app