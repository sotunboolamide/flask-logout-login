# -*- coding: utf-8 -*-
# @Author: sotunbo
# @Date:   2020-04-19 10:00:55
# @Last Modified by:   sotunbo
# @Last Modified time: 2020-04-21 13:52:29
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
CORS(app)