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
from datetime import datetime
import urllib.request, urllib.parse, json # For handaling json files
# from flask_mail import Mail, Message
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint, jsonify
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from flask import (Blueprint, Flask, flash, g, redirect, render_template,
                   request, send_file, session, url_for)
from flask_pymongo import PyMongo
from bson.json_util import dumps
import re
# from bs4 import BeautifulSoup
app= Flask(__name__)
app.config.from_pyfile('db.cfg')
app.url_map.strict_slashes = False
app.config['JSON_SORT_KEYS'] = False
Session(app)
mongo = PyMongo(app)


FILTER_ALLOWED_KEYS = [ 'created_at', 'updated_at', 'title', 'developer', 'price']
FILTER_ALLOWED_ORDER = {'asc': 1, 'desc': -1 }
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

def AppSerializer(cursor):
  res = []
  data = list(json.loads(dumps(list(cursor))))
  for app in data:
    res.append(
      {
        'id': app['id'],
        'title': app['title'],
        'icon': app['icon'],
        'developer': app['developer'],
        'price': app['price'],
        'url': app['url'],
        'developer_url': app['developer_url'],
        'developer_email': app['developer_email'],
        'created_at': app['created_at'],
        'updated_at': app['updated_at']
      }
    )
  return res

def AppListByIdsSerializer(cursor):
  data = [{ x['id']: x } for x in AppSerializer(cursor)]
  return data

def build_response(success=True, status_code=200, data=None, error=None, total_count=None):
  res = { 
    'success': success, 
    'error': error
  }
  if total_count is not None: res['total_count'] = total_count
  if data is not None: res['data'] = data
  return res, status_code

def get_filter_data(req={}):
  res = {  
    'page': '1',
    'limit': '20',
    'key': None,
    'order': None,
    'q': None
  }
  if len(req) != 0:
    # Pagination
    if int(req.get('page') or 0) > 0: res['page'] = req.get('page')
    if int(req.get('limit') or 0) > 0: res['limit'] = req.get('limit')
    # Sort
    if req.get('key') in FILTER_ALLOWED_KEYS: res['key'] = req.get('key')
    if FILTER_ALLOWED_ORDER.get(req.get('order')) is not None: res['order'] = FILTER_ALLOWED_ORDER.get(req.get('order'))
    # Search
    res['q'] = req.get('q')
  # Calculating offset
  res['offset'] = ((int(res['page']) - 1) * int(res['limit']))
  return res

def GetAppQuery(db, options={}):
  filters = options['filters']
  exp = None
  if filters['q'] is not None:
    q = filters['q'].replace('+', ' ')
    regx = re.compile(q, re.IGNORECASE)
    exp = {'$or': [{'title': regx}, {'developer': regx}, {'id': q}]}

  cursor = db.find(exp).limit(int(filters['limit'])).skip(int(filters['offset']))
  if filters['key'] is not None and filters['order'] is not None:
    cursor = cursor.sort(filters['key'], filters['order'])
  total_count = cursor.count()

  return cursor, total_count

def GetAppsFromIdsQuery(db, options={}):
  cursor = db.find({ 'id' : { '$in' : options['ids'] } })
  return cursor
# def get_a

# Importing Blueprints
from app_db.ios import ios
from app_db.play import play
from app_db.uwp import uwp

# Registering Blueprints
app.register_blueprint(ios,url_prefix='/api/ios')
app.register_blueprint(play,url_prefix='/api/play')
app.register_blueprint(uwp,url_prefix='/api/uwp')
