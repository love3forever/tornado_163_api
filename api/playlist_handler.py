#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_playlist_comment, parse_playlist_data)


class PlayelistDetailHandler(web.RequestHandler):
    async def get(self, playlist_id):
        try:
            playlist_data = await asyncio.ensure_future(parse_playlist_data(playlist_id))
        except:
            self.send_error()
        else:
            if not playlist_data:
                self.send_error(status_code=404)
            response = playlist_data
            self.write(response)


class PlaylistCommentsHandler(web.RequestHandler):
    async def get(self, playlist_id, page=1):
        try:
            playlist_comments_data = await asyncio.ensure_future(parse_playlist_comment(playlist_id, page=int(page)))
        except:
            self.send_error()
        else:
            if not playlist_comments_data:
                self.send_error(status_code=404)
            response = playlist_comments_data
            self.write(response)
