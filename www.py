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
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.user.Account import route_account

app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix='/user')
app.register_blueprint(route_static, url_prefix='/static')
app.register_blueprint(route_account, url_prefix='/account')
