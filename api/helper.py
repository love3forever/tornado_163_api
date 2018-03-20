#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

async def common_parse(handler, parse_func, *args, **kwargs):
    try:
        playlist_data =await parse_func(*args)
    except:
        handler.send_error()
    else:
        if not playlist_data:
            handler.send_error(status_code=404)
        response = playlist_data
        handler.write(response)
