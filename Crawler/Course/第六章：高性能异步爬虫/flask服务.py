#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/4/2020 10:06 PM
# __software__ : PyCharm

from flask import Flask
import time


app = Flask(__name__)


@app.route('/yixuan')
def index_bobo():
    time.sleep(2)
    return 'Hello yixuan'


@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'


if __name__ == '__main__':
    app.run(threaded=True)