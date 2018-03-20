#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_album_comments, parse_album_detail)
from api.helper import common_parse

class AlbumDetailHandler(web.RequestHandler):
    async def get(self, album_id):
        await common_parse(self,parse_album_detail,album_id)


class AlbumCommentsHandler(web.RequestHandler):
    async def get(self, album_id, page=1):
        await common_parse(self,parse_album_comments,album_id, page=int(page))
