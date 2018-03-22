#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio

from data_collector.data_parser import (parse_song_comments, parse_song_detail, parse_lyric_data)
from api.helper import RequestHandler


class SongDetailHanlder(RequestHandler):
    async def get(self, song_id):
        await self.make_response(parse_song_detail, song_id)


class SongCommnetsHandler(RequestHandler):
    async def get(self, song_id, page=1):
        await self.make_response(parse_song_comments, song_id, page=int(page))


class SongLyricHandler(RequestHandler):
    async def get(self, song_id):
        await self.make_response(parse_lyric_data, song_id)
