#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

from tornado import web,gen,httpclient
from datetime import datetime

class OriginHanlder(web.RequestHandler):
    @gen.coroutine
    def get(self):
        print(datetime.now())
        yield gen.sleep(5)
        data = yield httpclient.AsyncHTTPClient().fetch('http://localhost:4321/')
        self.write(data.body)

class OriginTestHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        print(datetime.now())
        yield gen.sleep(5)
        self.write('test')