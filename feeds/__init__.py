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
import urllib.request, json # For handling json files
# from flask_mail import Mail, Message
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for, session, Blueprint,jsonify
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from flask import (Blueprint, Flask, flash, g, redirect, render_template,
                   request, send_file, session, url_for)
import re
import psycopg2
import psycopg2.extras
# from bs4 import BeautifulSoup
app= Flask(__name__)
app.config.from_pyfile('db.cfg')
app.config['SESSION_FILE_DIR'] = mkdtemp()
app.url_map.strict_slashes = False
Session(app)
con = psycopg2.connect(dbname=app.config['DBNAME'],user=app.config['DBUSER'],host=app.config['HOST'],password=app.config['PASSWORD'])


def execute_db(query,args=()):
    cur=con.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute(query,args)
    con.commit()
    cur.close()

def query_db(query,args=(),one=False):
    cur=con.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute(query,args)
    res=cur.fetchall()
    con.commit()
    cur.close()
    if len(res)==0:
        return None
    if len(res)==1:
        return res[0]
    return res


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
from feeds.android.main import android

# Registering Blueprints
app.register_blueprint(android,url_prefix='/api/feeds/android/')

