#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/3122:29
文件:static.py
IDE:PyCharm
"""
from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint('static', __name__)


@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static", filename)
