#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/3120:17
文件:User.py
IDE:PyCharm
"""
from flask import Blueprint, render_template
route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return render_template("user/login.html")


@route_user.route("/edit")
def edit():
    return render_template("user/edit.html")


@route_user.route("/reset-pwd")
def reset_pwd():
    return render_template("user/reset_pwd.html")
