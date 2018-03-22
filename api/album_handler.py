#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_album_comments, parse_album_detail)
from api.helper import RequestHandler


class AlbumDetailHandler(RequestHandler):
    async def get(self, album_id):
        await self.make_response(parse_album_detail, album_id)


class AlbumCommentsHandler(RequestHandler):
    async def get(self, album_id, page=1):
        await self.make_response(parse_album_comments, album_id, page=int(page))
