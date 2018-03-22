#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from api.helper import RequestHandler
from data_collector.data_parser import (parse_artist_album, parse_artist_index_page)


class ArtistDetailHandler(RequestHandler):
    async def get(self, artist_id):
        await self.make_response(parse_artist_index_page, artist_id)


class ArtistAlbumHandler(RequestHandler):
    async def get(self, artist_id):
        await self.make_response(parse_artist_album, artist_id)
