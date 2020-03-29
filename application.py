#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/2919:04
文件:application.py
IDE:PyCharm
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        if "ConfigType" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ConfigType'])
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)

