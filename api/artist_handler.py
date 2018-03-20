#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_artist_album, parse_artist_index_page)
from api.helper import common_parse


class ArtistDetailHandler(web.RequestHandler):
    async def get(self, artist_id):
        await common_parse(self,parse_artist_index_page,artist_id)


class ArtistAlbumHandler(web.RequestHandler):
    async def get(self, artist_id):
        await common_parse(self,parse_artist_album,artist_id)
