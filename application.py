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
from common.libs.UrlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        self.config['JSON_AS_ASCII'] = False
        if "ConfigType" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ConfigType'])
        db.init_app(self)


db = SQLAlchemy()
app = Application(import_name=__name__, template_folder=os.getcwd()+"/web/templates/", root_path=os.getcwd())
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

manager = Manager(app)

""" 
函数模板
"""
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
