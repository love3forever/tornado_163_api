#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/20
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import asyncio
from tornado import web

from data_collector.data_parser import (parse_artist_album, parse_artist_index_page)


class ArtistDetailHandler(web.RequestHandler):
    async def get(self, artist_id):
        try:
            artist_detail_data = await asyncio.ensure_future(parse_artist_index_page(artist_id))
        except:
            self.send_error()
        else:
            if not artist_detail_data:
                self.send_error(status_code=404)
            response = artist_detail_data
            self.write(response)


class ArtistAlbumHandler(web.RequestHandler):
    async def get(self, artist_id):
        try:
            artist_album_data = await asyncio.ensure_future(parse_artist_album(artist_id))
        except:
            self.send_error()
        else:
            if not artist_album_data:
                self.send_error(status_code=404)
            response = {
                'artistId': artist_id,
                'albums': artist_album_data,
                'code': 200
            }
            self.write(response)
