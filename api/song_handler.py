#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_song_comments, parse_song_detail, parse_lyric_data)
from api.helper import common_parse

class SongDetailHanlder(web.RequestHandler):
    async def get(self, song_id):
        await common_parse(self,parse_song_detail,song_id)


class SongCommnetsHandler(web.RequestHandler):
    async def get(self, song_id, page=1):
        await common_parse(self,parse_song_comments,song_id, page=int(page))


class SongLyricHandler(web.RequestHandler):
    async def get(self, song_id):
        await common_parse(self,parse_lyric_data,song_id)
