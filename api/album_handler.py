#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_album_comments, parse_album_detail)


class AlbumDetailHandler(web.RequestHandler):
    async def get(self, album_id):
        try:
            album_detail_data = await asyncio.ensure_future(parse_album_detail(album_id))
        except:
            self.send_error()
        else:
            if not album_detail_data:
                self.send_error(status_code=404)
            response = album_detail_data
            self.write(response)


class AlbumCommentsHandler(web.RequestHandler):
    async def get(self, album_id, page=1):
        try:
            album_comments_data = await asyncio.ensure_future(parse_album_comments(album_id, page=int(page)))
        except:
            self.send_error()
        else:
            if not album_comments_data:
                self.send_error(status_code=404)
            response = album_comments_data
            self.write(response)
