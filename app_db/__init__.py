from __future__ import print_function
import csv
import pprint
import math
import os
import sys
import time
import requests
import json
import argparse
from datetime import date
import urllib.request, json # For handaling json files
# from flask_mail import Mail, Message
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for, session, Blueprint,jsonify
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from flask import (Blueprint, Flask, flash, g, redirect, render_template,
                   request, send_file, session, url_for)
from flask_pymongo import PyMongo
import re
# from bs4 import BeautifulSoup
app= Flask(__name__)
app.config.from_pyfile('db.cfg')
app.url_map.strict_slashes = False
Session(app)
mongo = PyMongo(app)

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("adminid") is None:
#             return redirect(url_for("auth.login"))
#         return f(*args, **kwargs)
#     return decorated_function

# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("admin")==False:
#             return redirect(url_for("main.index", next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function
    

# Importing Blueprints
from app_db.ios import ios
from app_db.play import play
# from app.views.scraping.flipkart import flipkart
# from app.views.scraping.youtube import youtube

# Registering Blueprints
app.register_blueprint(ios,url_prefix='/api/ios')
app.register_blueprint(play,url_prefix='/api/play')
# app.register_blueprint(flipkart)
# app.register_blueprint(youtube)
