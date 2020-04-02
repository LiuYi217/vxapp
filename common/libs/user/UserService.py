#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/4/222:55
文件:UserService.py
IDE:PyCharm
"""
import hashlib
import base64


class UserService:

    @staticmethod
    def gene_pwd(pwd, salt):
        """
        生成用户密码的加密算法
        :param pwd: 密码
        :param salt: 密钥
        :return:
        """
        m = hashlib.md5()
        str1 = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str1.encode("utf-8"))
        return m.hexdigest()
