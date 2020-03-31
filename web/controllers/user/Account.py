#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/3120:17
文件:User.py
IDE:PyCharm
"""
from flask import Blueprint, render_template
route_account = Blueprint('account_page', __name__)


@route_account.route("/index")
def index():
    return render_template("account/index.html")


@route_account.route("/info")
def info():
    return render_template("account/info.html")


@route_account.route("/set")
def set():
    return render_template("account/set.html")
