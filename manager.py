#!/usr/bin/python
# encoding: utf-8
"""
作者:糖葫芦
创建时间:2020/3/2919:05
文件:manager.py
IDE:PyCharm
"""
from application import app, manager
from flask_script import Server
import www

# web server
manager.add_command("runserver",
                    Server(host='0.0.0.0', port=app.config['SERVER_PORT'],
                           use_debugger=app.config['DEBUG'], use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
