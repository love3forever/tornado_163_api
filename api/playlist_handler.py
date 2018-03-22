#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from data_collector.data_parser import (parse_playlist_comment, parse_playlist_data)
from api.helper import RequestHandler


class PlayelistDetailHandler(RequestHandler):
    async def get(self, playlist_id):
        await self.make_response(parse_playlist_data, playlist_id)


class PlaylistCommentsHandler(RequestHandler):
    async def get(self, playlist_id, page=1):
        await self.make_response(parse_playlist_comment, playlist_id, page=int(page))
