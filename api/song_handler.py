#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_song_comments, parse_song_detail, parse_lyric_data)


class SongDetailHanlder(web.RequestHandler):
    async def get(self, song_id):
        try:
            song_detail_data = await asyncio.ensure_future(parse_song_detail(song_id))
        except:
            self.send_error()
        else:
            if not song_detail_data:
                self.send_error(status_code=404)
            response = song_detail_data
            self.write(response)


class SongCommnetsHandler(web.RequestHandler):
    async def get(self, song_id, page=1):
        try:
            song_comments_data = await asyncio.ensure_future(parse_song_comments(song_id, page=int(page)))
        except:
            self.send_error()
        else:
            if not song_comments_data:
                self.send_error(status_code=404)
            response = song_comments_data
            self.write(response)


class SongLyricHandler(web.RequestHandler):
    async def get(self, song_id):
        try:
            song_lryic_data = await asyncio.ensure_future(parse_lyric_data(song_id))
        except:
            self.send_error()
        else:
            if not song_lryic_data:
                self.send_error(status_code=404)
            response = song_lryic_data
            self.write(response)
