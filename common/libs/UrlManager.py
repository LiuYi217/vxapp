#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/3122:12
文件:UrlManager.py
IDE:PyCharm
"""


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%(22222)
        path = "/static" + path + "?ver" + ver
        return UrlManager.buildUrl(path)
