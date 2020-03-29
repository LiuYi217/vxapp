#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/2919:06
文件:www.py
IDE:PyCharm
"""
from application import app
from web.controllers.index import route_index

app.register_blueprint(route_index, url_prefix="/")
