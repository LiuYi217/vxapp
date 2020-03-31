#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/2922:50
文件:index.py
IDE:PyCharm
"""
from flask import Blueprint, render_template
route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    return render_template("index/index.html")
