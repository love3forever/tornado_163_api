#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

from tornado import web


class RequestHandler(web.RequestHandler):
    async def make_response(self, parse_func, *args, **kwargs):
        try:
            playlist_data = await parse_func(*args)
        except Exception as e:
            print(str(e))
            self.send_error()
        else:
            if not playlist_data:
                self.send_error(status_code=404)
            response = playlist_data
            self.write(response)
